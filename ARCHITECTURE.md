# CPUMiner-Multi Architecture

## Executive Summary
cpuminer-multi is a portable, multi-threaded CPU mining client written in C. The runtime is centered on `cpu-miner.c` (process lifecycle, CLI/config parsing, work scheduling, and mining threads), `util.c` (network/RPC + Stratum transport + shared utilities), and `api.c` (local/remote control API). Algorithm implementations are split across `algo/` and supporting crypto primitives under `crypto/`, `lyra2/`, `sha3/`, `scryptjane/`, and `yescrypt/`, with optional assembly accelerators in `asm/`.

The miner supports two upstream work models:
- JSON-RPC getwork/getblocktemplate style polling/longpoll
- Stratum (including JSON-RPC 2.0/XMR style login/job flow)

For DigiByte/DigiDollar solo mining, the relevant path is JSON-RPC
`getblocktemplate`. This fork keeps normal GBT requests legacy-safe by default
and only requests DigiDollar oracle-aware templates when the operator passes
`--digidollar`.

Core design choices favor portability and broad algorithm support over tight abstraction: algorithm dispatch is largely explicit switch-based routing in the mining loop, while transport and parsing are centralized in shared helpers.

## System Overview

```text
+--------------------+
| CLI + Config       |
| parse_arg/config   |
+---------+----------+
          |
          v
+--------------------+        +----------------------+
| Main Runtime       |        | API Thread (`api.c`) |
| `cpu-miner.c`      |<------>| summary/threads/etc  |
| - thread startup   |        | optional remote ctrl |
| - algo selection   |        +----------------------+
| - work scheduler   |
+----+-----------+---+
     |           |
     |           +--------------------+
     |                                |
     v                                v
+------------+                +------------------+
| WorkIO     |<-------------->| Network Layer    |
| thread     |  RPC submit    | `util.c`         |
| get/submit |--------------->| JSON-RPC/Stratum |
+------+-----+                +--------+---------+
       |                               |
       | work packages                 | socket/http
       v                               v
+-----------------------------------------------+
| Miner Threads (N)                              |
| nonce scan -> scanhash_* in `algo/*.c`         |
| verify target -> submit share/block            |
+----------------------+------------------------+
                       |
                       v
              +---------------------+
              | Pool / Node Backend |
              +---------------------+
```

## Directory Structure (validated)
Validated top-level source directories under `~/Code/cpuminer-multi`:
- `algo/`
- `api/`
- `asm/`
- `compat/`
- `crypto/`
- `lyra2/`
- `scryptjane/`
- `sha3/`
- `yescrypt/`
- `m4/`
- `res/`

Notable files:
- `cpu-miner.c` – entrypoint (`main`), option parsing, thread orchestration, mining loop.
- `miner.h` – global types, shared state, algorithm and utility declarations.
- `util.c` – logging, JSON-RPC client, Stratum protocol, queues, hashing test utilities.
- `api.c` – TCP/WebSocket API server for summary, thread stats, and optional remote controls.
- `compat/` – portability shims + bundled third-party headers/sources for Windows and fallback builds.

## Key Components

### 1) Runtime Control Plane (`cpu-miner.c`)
- Bootstraps process, detects capabilities, parses CLI/config (`parse_arg`, `parse_config`).
- Manages global options (algo, thread count, network endpoints, protocol toggles, affinity, benchmark/debug).
- Spawns and coordinates specialized threads:
  - Work I/O thread (`workio_thread`) for upstream fetch/submit.
  - Optional longpoll thread (`longpoll_thread`).
  - Optional Stratum thread (`stratum_thread`).
  - N mining workers (`miner_thread`).
- Chooses algorithm dispatch per worker via explicit `scanhash_*` routing.

### 2) Transport + Protocol Layer (`util.c`)
- HTTP JSON-RPC client (`json_rpc_call`), including headers/extensions and longpoll handling.
- Stratum socket lifecycle and parser:
  - connect/subscribe/authorize/read/write
  - methods: notify, difficulty, extranonce, reconnect, ping, client introspection
- JSON-RPC 2.0 path for CryptoNight-style pools (`rpc2_*`).
- Shared utilities:
  - hex/bin conversions, difficulty↔target helpers
  - queue primitives (`tq_*`) for inter-thread communication
  - logging helpers + hash diagnostics

### 3) DigiDollar GBT Handling (`cpu-miner.c`)
DigiDollar mint/redeem blocks require an oracle commitment in the coinbase when
the node provides one. This miner handles that without changing legacy behavior:

- The DigiByte/DigiDollar solo path in this fork covers `scrypt`, `sha256d`,
  `skein`, and `qubit`. It does not implement DigiByte `odo` / Odocrypt.
- Default GBT requests still advertise only `["segwit"]`.
- `--digidollar` changes normal and longpoll GBT requests to
  `["segwit","digidollar-oracle"]`.
- When a DD-aware template contains `default_oracle_commitment`, the miner adds
  it as a zero-value coinbase output while still building its own payout
  coinbase.
- If no `default_oracle_commitment` is present, the miner continues mining a
  normal DigiByte block. `--digidollar` does not make the miner an oracle and
  does not create oracle bundles by itself.
- Existing BIP22 `coinbasetxn` handling remains supported for templates that
  provide a complete coinbase transaction.

The GBT merkle code is intentionally txid-first:

- For non-coinbase template transactions, use the template `txid` field for the
  merkle leaf when it is present.
- Fall back to hashing raw transaction `data` only when no `txid` is supplied.
- Keep raw transaction `data` in the submitted block payload.

This matters because segwit transactions can include witness bytes in `data`,
while the block merkle tree commits to txids. Hashing raw witness-inclusive
transaction bytes would produce the wrong merkle root and can make an otherwise
valid block fail with `bad-txnmrklroot`.

The miner also encodes the BIP34 height in the generated coinbase script using
minimal CScript-style integer encoding. That keeps miner-built coinbases
compatible with modern DigiByte consensus rules.

### 4) Mining Algorithm Implementations (`algo/`)
- Each file typically exposes one or more `scanhash_*` and/or hash primitives.
- Families include:
  - SHA/Blake family: sha256d, blake/blakecoin/blake2*, decred, sia
  - X-series chains: x11/x12/x13/x14/x15/x16r/x16rv2/x16s/x17/x20r/xevan/x11evo
  - Memory-hard variants: scrypt, scrypt-jane, neoscrypt, yescrypt(+r8/r16/r32), cryptonight/light
  - Composite/chain algos: timetravel, bitcore, tribus, quark/qubit, lyra2* etc.

### 5) Crypto Primitives and Support Libraries
- `crypto/` – primitive hashes and compression functions.
- `sha3/`, `lyra2/`, `scryptjane/`, `yescrypt/` – specialized algorithm backends.
- `asm/` – optimized kernels (AES/SHA/scrypt/neoscrypt) for specific architectures.

### 6) External/API Surface (`api.c`, `api/*.php`)
- Local API server exposes summary and per-thread stats.
- Optional remote actions (`seturl`, `quit`) gated by API remote policy/IP ACL.
- Supports plain TCP command protocol and WebSocket handshake framing.

## End-to-End Data Flow
1. **Startup**: `main()` parses command-line + config; selects algorithm/network mode.
2. **Connection**:
   - JSON-RPC mode: work I/O requests work from daemon/pool.
   - Stratum mode: subscribe/authorize, receive notify jobs and difficulty updates.
3. **Work Distribution**: global/current work is copied into per-thread work context.
4. **Hashing Loop**: each miner thread calls algorithm-specific `scanhash_*`, iterating nonce ranges.
5. **Validation**: candidate hash checked against target (`fulltest` + difficulty/share ratio logic).
6. **Submission**: accepted shares submitted through work I/O/Stratum path.
7. **Telemetry**: hashrates/stats exported to console logs and optional API consumers.

## Configuration and Deployment
- **Build systems**: autotools (`configure.ac`, `Makefile.am`), helper scripts (`build.sh`, `autogen.sh`).
- **Primary runtime config**:
  - CLI args (algo, pool URL/user/pass, threads, protocol flags, debug/benchmark, API).
  - Optional JSON config file loading/parsing (`parse_config`, `json_load_url`).
- **Dependencies**:
  - libcurl, jansson, OpenSSL/libcrypto, pthreads (+ platform-specific compat layers).
- **Execution model**:
  - Single process, multiple pthread workers, lock-protected shared state.

## Technical Decisions and Trade-offs
- **Explicit switch dispatch for algos**: simple and predictable, at cost of extensibility abstraction.
- **Global shared state + mutexes**: straightforward C implementation, higher coupling.
- **Dual protocol support (getwork/longpoll + Stratum + rpc2)**: broad compatibility, more protocol complexity.
- **Bundled compatibility/vendor code**: easier Windows and legacy builds, larger source tree.
- **Optional assembly optimizations**: better throughput on supported CPUs, increased maintenance surface.

#!/usr/bin/env python3
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = (ROOT / 'cpu-miner.c').read_text()

WITNESS_TX_DATA = (
    '01000000'        # version
    '0001'            # segwit marker and flag
    '01'              # inputs
    + '00' * 32 +     # prevout hash
    '00000000'        # prevout index
    '00'              # empty scriptSig
    'ffffffff'        # sequence
    '01'              # outputs
    '0000000000000000'
    '01'
    '6a'              # OP_RETURN
    '01'              # witness stack items
    '02abcd'          # witness item
    '00000000'        # lock time
)


def sha256d(data: bytes) -> bytes:
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def witness_fixture_without_witness() -> bytes:
    tx = bytes.fromhex(WITNESS_TX_DATA)
    # version + inputs/outputs, without segwit marker/flag or witness stack
    return tx[:4] + tx[6:59] + tx[-4:]


def rpc_hash_from_internal(hash_bytes: bytes) -> str:
    return hash_bytes[::-1].hex()


def internal_hash_from_rpc(hex_hash: str) -> bytes:
    return bytes.fromhex(hex_hash)[::-1]


def encode_bip34_height(height: int) -> bytes:
    if not (height >= 1):
        raise ValueError('height must be positive')
    if height <= 16:
        return bytes([0x50 + height])
    out = bytearray()
    n = height
    while n:
        out.append(n & 0xff)
        n >>= 8
    if out[-1] & 0x80:
        out.append(0)
    return bytes(out)


def test_bip34_reference_vectors() -> None:
    assert encode_bip34_height(1) == bytes.fromhex('51')
    assert encode_bip34_height(16) == bytes.fromhex('60')
    assert encode_bip34_height(17) == bytes.fromhex('11')
    assert encode_bip34_height(127) == bytes.fromhex('7f')
    assert encode_bip34_height(128) == bytes.fromhex('8000')
    assert encode_bip34_height(255) == bytes.fromhex('ff00')
    assert encode_bip34_height(256) == bytes.fromhex('0001')


def test_source_has_small_integer_fast_path() -> None:
    assert 'work->height >= 1 && work->height <= 16' in SOURCE
    assert 'cbtx[42] = 0x50 + work->height' in SOURCE
    assert 'if (cbtx[cbtx_size - 1] & 0x80)' in SOURCE


def test_getblocktemplate_requests_advertise_segwit() -> None:
    assert '#define GBT_RULES "[\\"segwit\\"]"' in SOURCE
    assert re.search(r'GBT_CAPABILITIES ", \\"rules\\": " GBT_RULES', SOURCE)


def test_witness_transaction_fixture_needs_txid_leaf_not_raw_hash() -> None:
    raw_leaf = sha256d(bytes.fromhex(WITNESS_TX_DATA))
    txid = rpc_hash_from_internal(sha256d(witness_fixture_without_witness()))
    txid_leaf = internal_hash_from_rpc(txid)

    assert raw_leaf != txid_leaf
    assert 'hash[i] = tmp[31 - i];' in SOURCE
    assert re.search(r'gbt_decode_hash\s*\(\s*merkle_tree\[1 \+ i\]\s*,\s*txid_hex\s*\)', SOURCE)
    assert re.search(r'if\s*\(\s*txid_hex\s*\).*strlen\s*\(\s*txid_hex\s*\)\s*!=\s*64', SOURCE, re.S)


def test_gbt_submit_payload_still_appends_raw_transaction_data() -> None:
    assert '0001' in WITNESS_TX_DATA
    assert re.search(r'if \(!submit_coinbase\)\s*strcat\(work->txs, tx_hex\);', SOURCE)


def test_digidollar_gbt_is_explicit_opt_in() -> None:
    assert '#define GBT_RULES "[\\"segwit\\"]"' in SOURCE
    assert '#define GBT_DIGIDOLLAR_RULES "[\\"segwit\\",\\"digidollar-oracle\\"]"' in SOURCE
    assert '{ "digidollar", 0, NULL,' in SOURCE
    assert 'opt_digidollar ? gbt_digidollar_req : gbt_req' in SOURCE
    assert 'opt_digidollar ? gbt_digidollar_lp_req : gbt_lp_req' in SOURCE


def test_default_commitments_are_preserved_in_miner_built_coinbase() -> None:
    assert re.search(
        r'json_object_get\s*\(\s*val\s*,\s*"default_witness_commitment"\s*\).*'
        r'gbt_append_commitment_output',
        SOURCE,
        re.S,
    )
    assert re.search(
        r'opt_digidollar.*json_object_get\s*\(\s*val\s*,\s*"default_oracle_commitment"\s*\).*'
        r'gbt_append_commitment_output',
        SOURCE,
        re.S,
    )


if __name__ == '__main__':
    test_bip34_reference_vectors()
    test_source_has_small_integer_fast_path()
    test_getblocktemplate_requests_advertise_segwit()
    test_witness_transaction_fixture_needs_txid_leaf_not_raw_hash()
    test_gbt_submit_payload_still_appends_raw_transaction_data()
    test_digidollar_gbt_is_explicit_opt_in()
    test_default_commitments_are_preserved_in_miner_built_coinbase()
    print('ok')

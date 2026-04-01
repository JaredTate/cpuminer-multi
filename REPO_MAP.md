# CPUMiner-Multi Repository Map

Generated from on-disk files in `~/Code/cpuminer-multi` (paths validated).

### Android.mk
- Role: build/config source

### Makefile
- Role: build/config source

### Makefile.am
- Role: build/config source

### Makefile.in
- Role: build/config source

### aclocal.m4
- Role: build/config source

### algo/allium.c
- Functions: allium_hash, scanhash_allium
- Types: work

### algo/axiom.c
- Functions: axiomhash, scanhash_axiom
- Types: work

### algo/bastion.c
- Functions: bastionhash, scanhash_bastion
- Types: work

### algo/bitcore.c
- Functions: swap, reverse, next_permutation, bitcore_hash, scanhash_bitcore
- Types: work
- Macros: HASH_FUNC_BASE_TIMESTAMP, HASH_FUNC_COUNT, HASH_FUNC_COUNT_PERMUTATIONS

### algo/blake.c
- Functions: blakehash, scanhash_blake
- Types: work

### algo/blake2.c
- Functions: blake2s_hash, blake2s_hash_end, scanhash_blake2s
- Types: work
- Macros: MIDLEN, A

### algo/blake2b.c
- No exported symbols detected; file provides local implementation details.

### algo/blakecoin.c
- Functions: blakecoin_init, blakecoin, blakecoin_close, blakecoinhash, scanhash_blakecoin
- Types: work
- Macros: BLAKE32_ROUNDS

### algo/bmw256.c
- Functions: bmwhash, scanhash_bmw
- Types: work

### algo/c11.c
- Functions: c11hash, scanhash_c11
- Types: work

### algo/cryptolight.c
- Functions: __attribute__, do_blake_hash, do_groestl_hash, do_jh_hash, do_skein_hash, aesb_single_round, aesb_pseudo_round_mut, fast_aesb_single_round, fast_aesb_pseudo_round_mut, mul128, e2i, mul_sum_xor_dst, xor_blocks, xor_blocks_dst, cryptolight_store_variant, cryptolight_hash_ctx, cryptolight_hash, cryptolight_hash_ctx_aes_ni, scanhash_cryptolight
- Types: cn_slow_hash_state, hash_state, cryptonight_ctx, work
- Macros: NOASM, USE_INT128, LITE, MEMORY, ITER, AES_BLOCK_SIZE, AES_KEY_SIZE, INIT_SIZE_BLK, INIT_SIZE_BYTE, fast_aesb_single_round, fast_aesb_pseudo_round_mut

### algo/cryptonight.c
- Functions: __attribute__, do_blake_hash, do_groestl_hash, do_jh_hash, do_skein_hash, aesb_single_round, aesb_pseudo_round_mut, fast_aesb_single_round, fast_aesb_pseudo_round_mut, mul128, e2i, mul_sum_xor_dst, xor_blocks, xor_blocks_dst, cryptonight_store_variant, cryptonight_hash_ctx, cryptonight_hash, cryptonight_hash_v1, cryptonight_hash_ctx_aes_ni, scanhash_cryptonight
- Types: cn_slow_hash_state, hash_state, cryptonight_ctx, work
- Macros: NOASM, USE_INT128, LITE, MEMORY, ITER, AES_BLOCK_SIZE, AES_KEY_SIZE, INIT_SIZE_BLK, INIT_SIZE_BYTE, fast_aesb_single_round, fast_aesb_pseudo_round_mut

### algo/decred.c
- Functions: decred_hash, decred_hash_simple, scanhash_decred
- Types: work
- Macros: MIDSTATE_LEN, DCR_NONCE_OFT32

### algo/drop.c
- Functions: shiftr_lp, switchHash, droplp_hash, droplp_hash_pok, scanhash_drop
- Types: work
- Macros: POK_BOOL_MASK, POK_DATA_MASK, tmpdata

### algo/fresh.c
- Functions: freshhash, scanhash_fresh
- Types: work
- Macros: hashA, hashB

### algo/geek.c
- Functions: geekhash, scanhash_geek
- Types: work

### algo/groestl.c
- Functions: groestlhash, scanhash_groestl
- Types: work

### algo/heavy.c
- Functions: combine_hashes, heavyhash, scanhash_heavy
- Types: work

### algo/ink.c
- Functions: inkhash, scanhash_ink
- Types: work

### algo/jha.c
- Functions: jha_hash, scanhash_jha
- Types: work

### algo/keccak.c
- Functions: keccakhash, scanhash_keccak
- Types: work

### algo/lbry.c
- Functions: lbry_initstate, lbry_hash, scanhash_lbry
- Types: work
- Macros: A

### algo/luffa.c
- Functions: luffahash, scanhash_luffa
- Types: work

### algo/lyra2re.c
- Functions: lyra2_hash, scanhash_lyra2
- Types: work

### algo/lyra2rev2.c
- Functions: lyra2rev2_hash, scanhash_lyra2rev2
- Types: work

### algo/lyra2v3.c
- Functions: lyra2v3_hash, scanhash_lyra2v3
- Types: work

### algo/myr-groestl.c
- Functions: myriadhash, scanhash_myriad
- Types: work

### algo/neoscrypt.c
- Functions: sha256_blocks, neoscrypt_hash_init_sha256, neoscrypt_hash_update_sha256, neoscrypt_hash_finish_sha256, neoscrypt_hash_sha256, neoscrypt_hmac_init_sha256, neoscrypt_hmac_update_sha256, neoscrypt_hmac_finish_sha256, neoscrypt_pbkdf2_sha256, neoscrypt_salsa, neoscrypt_salsa_tangle, neoscrypt_chacha, neoscrypt_blkcpy, neoscrypt_blkswp, neoscrypt_blkxor, neoscrypt_copy, neoscrypt_erase, neoscrypt_xor, blake2s_compress, blake2s_update, neoscrypt_blake2s, neoscrypt_fastkdf, neoscrypt_blkmix, neoscrypt, fulltest_le, scanhash_neoscrypt
- Types: sha256_hash_state_t, sha256_hmac_state_t, blake2s_param_t, blake2s_state_t, work
- Macros: USE_CUSTOM_BLAKE2S, STACK_ALIGN, ASM, MIN, MAX, SCRYPT_BLOCK_SIZE, SCRYPT_HASH_BLOCK_SIZE, SCRYPT_HASH_DIGEST_SIZE, ROTL32, ROTR32, U8TO32_BE, U32TO8_BE, U64TO8_BE, Ch, Maj, S0, S1, G0, G1, W0, W1, STEP, quarter, BLAKE2S_BLOCK_SIZE, BLAKE2S_OUT_SIZE, BLAKE2S_KEY_SIZE, G, ROUND, FASTKDF_BUFFER_SIZE, kdf_buf_size, prf_input_size, prf_key_size, prf_output_size

### algo/nist5.c
- Functions: nist5hash, scanhash_nist5
- Types: work

### algo/pentablake.c
- Functions: pentablakehash, scanhash_pentablake
- Types: work
- Macros: hashB

### algo/phi1612.c
- Functions: phi1612_hash, scanhash_phi1612
- Types: work

### algo/phi2.c
- Functions: phi2_hash, scanhash_phi2
- Types: work

### algo/pluck.c
- Functions: xor_salsa8, sha256_transform_volatile, sha256_hash, sha256_hash512, pluck_hash, scanhash_pluck
- Types: work
- Macros: BLOCK_HEADER_SIZE, htobe32, ROTL, ROTR, _VECTOR, OPT_COMPATIBLE, Ch, Maj, S0, S1, s0, s1, RND, RNDr

### algo/quark.c
- Functions: init_quarkhash_contexts, quarkhash, scanhash_quark
- Types: work

### algo/qubit.c
- Functions: qubithash, scanhash_qubit
- Types: work

### algo/rainforest.c
- Functions: add_round_key, sub_bytes, shift_rows, mix_columns, rotate32, sbox, aes2r_encrypt, volatile, rf_crc32_32, rf_add64_crc32, rf_crc32x4, rf_memr64, rf_wltable, rf_whtable, rf_rotl64, rf_rotr64, rf_bswap64, rf_rambox, rf_w128, rf_raminit, rf256_divbox, rf256_rotbox, rf256_scramble, rf256_inject, rf256_rot32x256, rf256_aesenc, rf256_one_round, rf256_init, rf256_update, rf256_final, rf256_hash, scanhash_rf256
- Types: _ALIGN, work
- Macros: RAMBOX_SIZE, RAMBOX_LOOPS, RAMBOX_HIST, RF_UNALIGNED_LE64, RF_UNALIGNED_LE32, RF256_INIT_CRC

### algo/s3.c
- Functions: s3hash, scanhash_s3
- Types: work

### algo/scrypt-jane.c
- Functions: scrypt_alloc, scrypt_free, scrypt_N_1_1, GetNfactor, scanhash_scryptjane, scryptjanehash
- Types: scrypt_aligned_alloc_t, work
- Macros: SCRYPT_R, SCRYPT_P, CPU_X86_FORCE_INTRINSICS, SCRYPT_KECCAK512, SCRYPT_CHACHA, SCRYPT_CHOOSE_COMPILETIME, scrypt_maxN, scrypt_r_32kb, scrypt_maxr, scrypt_maxp

### algo/scrypt.c
- Functions: HMAC_SHA256_80_init, PBKDF2_SHA256_80_128, PBKDF2_SHA256_128_32, HMAC_SHA256_80_init_4way, PBKDF2_SHA256_80_128_4way, PBKDF2_SHA256_128_32_4way, HMAC_SHA256_80_init_8way, PBKDF2_SHA256_80_128_8way, PBKDF2_SHA256_128_32_8way, scrypt_best_throughput, scrypt_core, scrypt_core_3way, scrypt_core_6way, xor_salsa8, scrypt_1024_1_1_256, scrypt_1024_1_1_256_4way, scrypt_1024_1_1_256_3way, scrypt_1024_1_1_256_12way, scrypt_1024_1_1_256_24way, scanhash_scrypt, scrypthash
- Types: work
- Macros: SCRYPT_MAX_WAYS, HAVE_SCRYPT_3WAY, HAVE_SCRYPT_6WAY, scrypt_best_throughput, R

### algo/sha2.c
- Functions: sha256_init, sha256_transform, sha256d_80_swap, sha256d, sha256d_preextend, sha256d_prehash, sha256d_ms, sha256d_ms_4way, scanhash_sha256d_4way, sha256d_ms_8way, scanhash_sha256d_8way, scanhash_sha256d
- Types: work
- Macros: EXTERN_SHA256, Ch, Maj, ROTR, S0, S1, s0, s1, RND, RNDr

### algo/sia.c
- Functions: blake2b_hash_end, blake2b_hash, scanhash_blake2b, swab256, scanhash_sia
- Types: work
- Macros: A, MIDLEN

### algo/sibcoin.c
- Functions: sibhash, scanhash_sib
- Types: work

### algo/skein.c
- Functions: skeinhash, scanhash_skein
- Types: work

### algo/skein2.c
- Functions: skein2hash, scanhash_skein2
- Types: work

### algo/sonoa.c
- Functions: sonoa_hash, scanhash_sonoa
- Types: work

### algo/timetravel.c
- Functions: swap, reverse, next_permutation, timetravel_hash, scanhash_timetravel
- Types: work
- Macros: HASH_FUNC_BASE_TIMESTAMP, HASH_FUNC_COUNT, HASH_FUNC_COUNT_PERMUTATIONS

### algo/tribus.c
- Functions: tribus_hash, scanhash_tribus
- Types: work

### algo/veltor.c
- Functions: init_Xhash_contexts, veltor_hash, scanhash_veltor
- Types: work

### algo/x11.c
- Functions: x11hash, scanhash_x11
- Types: work

### algo/x11evo.c
- Functions: swap8, initPerm, nextPerm, getAlgoString, sprintf, getCurrentAlgoSeq, evo_twisted_code, x11evo_hash, scanhash_x11evo
- Types: Algo, work
- Macros: INITIAL_DATE

### algo/x12.c
- Functions: x12hash, scanhash_x12
- Types: work

### algo/x13.c
- Functions: x13hash, scanhash_x13
- Types: work
- Macros: hashB

### algo/x14.c
- Functions: x14hash, scanhash_x14
- Types: work
- Macros: hashB

### algo/x15.c
- Functions: x15hash, scanhash_x15
- Types: work
- Macros: hashB

### algo/x16r.c
- Functions: getAlgoString, sprintf, x16r_hash, scanhash_x16r
- Types: Algo, work

### algo/x16rv2.c
- Functions: getAlgoString, sprintf, padtiger512, x16rv2_hash, scanhash_x16rv2
- Types: Algo, work

### algo/x16s.c
- Functions: getAlgoString, x16s_hash, scanhash_x16s
- Types: Algo, work

### algo/x17.c
- Functions: x17hash, scanhash_x17
- Types: work

### algo/x20r.c
- Functions: getAlgoString, sprintf, x20r_hash, scanhash_x20r
- Types: Algo, work

### algo/xevan.c
- Functions: xevan_hash, scanhash_xevan
- Types: work

### algo/yescrypt.c
- Functions: do_scanhash, scanhash_yescrypt, scanhash_yescryptr8, scanhash_yescryptr16, scanhash_yescryptr32
- Types: work

### algo/zr5.c
- Functions: zr5hash, zr5hash_pok, scanhash_zr5
- Types: work
- Macros: ZR_BLAKE, ZR_GROESTL, ZR_JH512, ZR_SKEIN, POK_BOOL_MASK, POK_DATA_MASK, tmpdata

### api.c
- Functions: cpu_temp, cpu_clock, cpu_fanpercent, cpustatus, check_remote_access, send_result, base64_encode, websocket_handshake, setup_ipaccess, check_connect, api
- Types: APIGROUPS, IP4ACCESS, cpu_info, CMDS, sockaddr_in, sockaddr, thr_info
- Macros: APIVERSION, _WINSOCK_DEPRECATED_NO_WARNINGS, SOCKETTYPE, SOCKETFAIL, INVSOCK, INVINETADDR, CLOSESOCKET, SOCKETINIT, SOCKERRMSG, in_addr_t, GROUP, PRIVGROUP, NOPRIVGROUP, ISPRIVGROUP, GROUPOFFSET, VALIDGROUP, COMMANDS, DEFINEDGROUP, MYBUFSIZ, SOCK_REC_BUFSZ, QUEUE, ALLIP4, cpu_threads, USE_MONITORING, CMDMAX

### api/index.php
- Functions: getdataFromPears, ignoreField, translateField, translateValue, displayData

### api/local-sample.php
- Functions: getsock, readsockline, request

### asm/aesb-x64.S
- Exports: fast_aesb_single_round, _fast_aesb_single_round, fast_aesb_pseudo_round_mut, _fast_aesb_pseudo_round_mut, mul128, _mul128

### asm/aesb-x86.S
- Exports: fast_aesb_single_round, _fast_aesb_single_round, fast_aesb_pseudo_round_mut, _fast_aesb_pseudo_round_mut

### asm/neoscrypt_asm.S
- Exports: neoscrypt_blkcpy, _neoscrypt_blkcpy, neoscrypt_blkswp, _neoscrypt_blkswp, neoscrypt_blkxor, _neoscrypt_blkxor, neoscrypt_salsa, _neoscrypt_salsa, neoscrypt_salsa_tangle, _neoscrypt_salsa_tangle, neoscrypt_chacha, _neoscrypt_chacha

### asm/scrypt-arm.S
- Exports: scrypt_core, _scrypt_core, scrypt_core_3way, _scrypt_core_3way

### asm/scrypt-x64.S
- Exports: scrypt_best_throughput, _scrypt_best_throughput, scrypt_core, _scrypt_core, scrypt_core_3way, _scrypt_core_3way, scrypt_core_6way, _scrypt_core_6way

### asm/scrypt-x86.S
- Exports: scrypt_core, _scrypt_core

### asm/sha2-arm.S
- Exports: sha256_transform, _sha256_transform, sha256d_ms, _sha256d_ms, sha256_init_4way, _sha256_init_4way, sha256_transform_4way, _sha256_transform_4way, sha256d_ms_4way, _sha256d_ms_4way, sha256_use_4way, _sha256_use_4way

### asm/sha2-x64.S
- Exports: sha256_init_4way, _sha256_init_4way, sha256_init_8way, _sha256_init_8way, sha256_transform_4way, _sha256_transform_4way, sha256_transform_8way, _sha256_transform_8way, sha256d_ms_4way, _sha256d_ms_4way, sha256_use_4way, _sha256_use_4way, sha256d_ms_8way, _sha256d_ms_8way, sha256_use_8way, _sha256_use_8way

### asm/sha2-x86.S
- Exports: sha256_init_4way, _sha256_init_4way, sha256_transform_4way, _sha256_transform_4way, sha256d_ms_4way, _sha256d_ms_4way, sha256_use_4way, _sha256_use_4way

### autogen.sh
- Entry: script entrypoint

### build-linux-arm.sh
- Entry: script entrypoint

### build.sh
- Entry: script entrypoint

### compat.h
- Functions: setpriority, msver, dirname
- Macros: __COMPAT_H__, localtime_r, sleep, snprintf, strdup, strncasecmp, strcasecmp, __func__, __thread, _ALIGN, unlikely, likely, MAX_PATH

### compat/Makefile.am
- Role: build/config source

### compat/Makefile.in
- Role: build/config source

### compat/bionic/cpuminer-config.h
- Macros: HAVE_ALLOCA, HAVE_ALLOCA_H, HAVE_DECL_BE32DEC, HAVE_DECL_BE32ENC, HAVE_DECL_LE16DEC, HAVE_DECL_LE16ENC, HAVE_DECL_LE32DEC, HAVE_DECL_LE32ENC, HAVE_GETOPT_LONG, HAVE_INTTYPES_H, HAVE_MEMORY_H, HAVE_STDINT_H, HAVE_STDLIB_H, HAVE_STRINGS_H, HAVE_STRING_H, HAVE_SYSLOG_H, HAVE_SYS_PARAM_H, HAVE_SYS_STAT_H, HAVE_SYS_TYPES_H, HAVE_UNISTD_H, PACKAGE, PACKAGE_BUGREPORT, PACKAGE_NAME, PACKAGE_STRING, PACKAGE_TARNAME, PACKAGE_URL, PACKAGE_VERSION, STDC_HEADERS, USE_ASM, USE_AVX, USE_AVX2, USE_XOP

### compat/cpuminer-config.h
- Macros: HAVE_ALLOCA, HAVE_DECL_BE32DEC, HAVE_DECL_BE32ENC, HAVE_DECL_LE16DEC, HAVE_DECL_LE16ENC, HAVE_DECL_LE32DEC, HAVE_DECL_LE32ENC, HAVE_GETOPT_LONG, HAVE_INTTYPES_H, HAVE_MEMORY_H, HAVE_STDINT_H, HAVE_STDLIB_H, HAVE_STRINGS_H, HAVE_STRING_H, HAVE_SYS_PARAM_H, HAVE_SYS_STAT_H, HAVE_SYS_TYPES_H, HAVE_UNISTD_H, PACKAGE, PACKAGE_BUGREPORT, PACKAGE_NAME, PACKAGE_STRING, PACKAGE_TARNAME, PACKAGE_URL, PACKAGE_VERSION, STDC_HEADERS, USE_ASM, USE_AVX, USE_AVX2, USE_INT128, USE_XOP, VERSION

### compat/curl-for-windows/curl/include/curl/curl.h
- Functions: int, size_t, downloading, long, curl_socket_t, curlioerr, void, CURLcode, curl_formadd, curl_formget, curl_formfree, curl_free, curl_global_init, curl_global_init_mem, curl_global_cleanup, curl_slist_free_all, curl_getdate, curl_share_setopt, curl_share_cleanup, curl_easy_pause
- Types: curl_httppost, curl_slist, curl_fileinfo, curl_sockaddr, sockaddr, existed, was, curl_khtype, curl_khkey, curl_khstat, curl_khmatch, CURL_NETRC_OPTION, CURL_TLSAUTH, curl_forms, failed, cannot, built, curl_certinfo, for, curl_tlssessioninfo, the, ever, from
- Macros:
  - `__CURL_CURL_H`
  - `WIN32`
  - `CURL_EXTERN`
  - `CURL_SOCKET_BAD`
  - `curl_socket_typedef`
  - `HTTPPOST_FILENAME`
  - `HTTPPOST_READFILE`
  - `HTTPPOST_PTRNAME`
  - `HTTPPOST_PTRCONTENTS`
  - `HTTPPOST_BUFFER`
  - `HTTPPOST_PTRBUFFER`
  - `HTTPPOST_CALLBACK`
  - `CURL_MAX_WRITE_SIZE`
  - `CURL_MAX_HTTP_HEADER`
  - `CURL_WRITEFUNC_PAUSE`
  - `CURLFINFOFLAG_KNOWN_FILENAME`
  - `CURLFINFOFLAG_KNOWN_FILETYPE`
  - `CURLFINFOFLAG_KNOWN_TIME`
  - `CURLFINFOFLAG_KNOWN_PERM`
  - `CURLFINFOFLAG_KNOWN_UID`
  - `CURLFINFOFLAG_KNOWN_GID`
  - `CURLFINFOFLAG_KNOWN_SIZE`
  - `CURLFINFOFLAG_KNOWN_HLINKCOUNT`
  - `CURL_CHUNK_BGN_FUNC_OK`
  - `CURL_CHUNK_BGN_FUNC_FAIL`
  - `CURL_CHUNK_BGN_FUNC_SKIP`
  - `CURL_CHUNK_END_FUNC_OK`
  - `CURL_CHUNK_END_FUNC_FAIL`
  - `CURL_FNMATCHFUNC_MATCH`
  - `CURL_FNMATCHFUNC_NOMATCH`
  - `CURL_FNMATCHFUNC_FAIL`
  - `CURL_SEEKFUNC_OK`
  - `CURL_SEEKFUNC_FAIL`
  - `CURL_SEEKFUNC_CANTSEEK`
  - `CURL_READFUNC_ABORT`
  - `CURL_READFUNC_PAUSE`
  - `CURL_SOCKOPT_OK`
  - `CURL_SOCKOPT_ERROR`
  - `CURL_SOCKOPT_ALREADY_CONNECTED`
  - `CURLE_OBSOLETE16`
  - `CURLE_OBSOLETE10`
  - `CURLE_OBSOLETE12`
  - `CURLOPT_ENCODING`
  - `CURLE_UNKNOWN_TELNET_OPTION`
  - `CURLE_SSL_PEER_CERTIFICATE`
  - `CURLE_OBSOLETE`
  - `CURLE_BAD_PASSWORD_ENTERED`
  - `CURLE_BAD_CALLING_ORDER`
  - `CURLE_FTP_USER_PASSWORD_INCORRECT`
  - `CURLE_FTP_CANT_RECONNECT`
  - `CURLE_FTP_COULDNT_GET_SIZE`
  - `CURLE_FTP_COULDNT_SET_ASCII`
  - `CURLE_FTP_WEIRD_USER_REPLY`
  - `CURLE_FTP_WRITE_ERROR`
  - `CURLE_LIBRARY_NOT_FOUND`
  - `CURLE_MALFORMAT_USER`
  - `CURLE_SHARE_IN_USE`
  - `CURLE_URL_MALFORMAT_USER`
  - `CURLE_FTP_ACCESS_DENIED`
  - `CURLE_FTP_COULDNT_SET_BINARY`
  - `CURLE_FTP_QUOTE_ERROR`
  - `CURLE_TFTP_DISKFULL`
  - `CURLE_TFTP_EXISTS`
  - `CURLE_HTTP_RANGE_ERROR`
  - `CURLE_FTP_SSL_FAILED`
  - `CURLE_OPERATION_TIMEOUTED`
  - `CURLE_HTTP_NOT_FOUND`
  - `CURLE_HTTP_PORT_FAILED`
  - `CURLE_FTP_COULDNT_STOR_FILE`
  - `CURLE_FTP_PARTIAL_FILE`
  - `CURLE_FTP_BAD_DOWNLOAD_RESUME`
  - `CURLE_ALREADY_COMPLETE`
  - `CURLOPT_FILE`
  - `CURLOPT_INFILE`
  - `CURLOPT_WRITEHEADER`
  - `CURLOPT_WRITEINFO`
  - `CURLOPT_CLOSEPOLICY`
  - `CURLAUTH_NONE`
  - `CURLAUTH_BASIC`
  - `CURLAUTH_DIGEST`
  - `CURLAUTH_NEGOTIATE`
  - `CURLAUTH_GSSNEGOTIATE`
  - `CURLAUTH_NTLM`
  - `CURLAUTH_DIGEST_IE`
  - `CURLAUTH_NTLM_WB`
  - `CURLAUTH_ONLY`
  - `CURLAUTH_ANY`
  - `CURLAUTH_ANYSAFE`
  - `CURLSSH_AUTH_ANY`
  - `CURLSSH_AUTH_NONE`
  - `CURLSSH_AUTH_PUBLICKEY`
  - `CURLSSH_AUTH_PASSWORD`
  - `CURLSSH_AUTH_HOST`
  - `CURLSSH_AUTH_KEYBOARD`
  - `CURLSSH_AUTH_AGENT`
  - `CURLSSH_AUTH_DEFAULT`
  - `CURLGSSAPI_DELEGATION_NONE`
  - `CURLGSSAPI_DELEGATION_POLICY_FLAG`
  - `CURLGSSAPI_DELEGATION_FLAG`
  - `CURL_ERROR_SIZE`
  - `CURLSSLOPT_ALLOW_BEAST`
  - `CURLFTPSSL_NONE`
  - `CURLFTPSSL_TRY`
  - `CURLFTPSSL_CONTROL`
  - `CURLFTPSSL_ALL`
  - `CURLFTPSSL_LAST`
  - `curl_ftpssl`
  - `CURLHEADER_UNIFIED`
  - `CURLHEADER_SEPARATE`
  - `CURLPROTO_HTTP`
  - `CURLPROTO_HTTPS`
  - `CURLPROTO_FTP`
  - `CURLPROTO_FTPS`
  - `CURLPROTO_SCP`
  - `CURLPROTO_SFTP`
  - `CURLPROTO_TELNET`
  - `CURLPROTO_LDAP`
  - `CURLPROTO_LDAPS`
  - `CURLPROTO_DICT`
  - `CURLPROTO_FILE`
  - `CURLPROTO_TFTP`
  - `CURLPROTO_IMAP`
  - `CURLPROTO_IMAPS`
  - `CURLPROTO_POP3`
  - `CURLPROTO_POP3S`
  - `CURLPROTO_SMTP`
  - `CURLPROTO_SMTPS`
  - `CURLPROTO_RTSP`
  - `CURLPROTO_RTMP`
  - `CURLPROTO_RTMPT`
  - `CURLPROTO_RTMPE`
  - `CURLPROTO_RTMPTE`
  - `CURLPROTO_RTMPS`
  - `CURLPROTO_RTMPTS`
  - `CURLPROTO_GOPHER`
  - `CURLPROTO_ALL`
  - `CURLOPTTYPE_LONG`
  - `CURLOPTTYPE_OBJECTPOINT`
  - `CURLOPTTYPE_FUNCTIONPOINT`
  - `CURLOPTTYPE_OFF_T`
  - `CINIT`
  - `LONG`
  - `OBJECTPOINT`
  - `FUNCTIONPOINT`
  - `OFF_T`
  - `CURLOPT_XFERINFODATA`
  - `CURLOPT_SERVER_RESPONSE_TIMEOUT`
  - `CURLOPT_POST301`
  - `CURLOPT_SSLKEYPASSWD`
  - `CURLOPT_FTPAPPEND`
  - `CURLOPT_FTPLISTONLY`
  - `CURLOPT_FTP_SSL`
  - `CURLOPT_SSLCERTPASSWD`
  - `CURLOPT_KRB4LEVEL`
  - `CURL_IPRESOLVE_WHATEVER`
  - `CURL_IPRESOLVE_V4`
  - `CURL_IPRESOLVE_V6`
  - `CURLOPT_RTSPHEADER`
  - `CURL_REDIR_GET_ALL`
  - `CURL_REDIR_POST_301`
  - `CURL_REDIR_POST_302`
  - `CURL_REDIR_POST_303`
  - `CURL_REDIR_POST_ALL`
  - `CFINIT`
  - `CURLINFO_STRING`
  - `CURLINFO_LONG`
  - `CURLINFO_DOUBLE`
  - `CURLINFO_SLIST`
  - `CURLINFO_MASK`
  - `CURLINFO_TYPEMASK`
  - `CURLINFO_HTTP_CODE`
  - `CURL_GLOBAL_SSL`
  - `CURL_GLOBAL_WIN32`
  - `CURL_GLOBAL_ALL`
  - `CURL_GLOBAL_NOTHING`
  - `CURL_GLOBAL_DEFAULT`
  - `CURL_GLOBAL_ACK_EINTR`
  - `CURLVERSION_NOW`
  - `CURL_VERSION_IPV6`
  - `CURL_VERSION_KERBEROS4`
  - `CURL_VERSION_SSL`
  - `CURL_VERSION_LIBZ`
  - `CURL_VERSION_NTLM`
  - `CURL_VERSION_GSSNEGOTIATE`
  - `CURL_VERSION_DEBUG`
  - `CURL_VERSION_ASYNCHDNS`
  - `CURL_VERSION_SPNEGO`
  - `CURL_VERSION_LARGEFILE`
  - `CURL_VERSION_IDN`
  - `CURL_VERSION_SSPI`
  - `CURL_VERSION_CONV`
  - `CURL_VERSION_CURLDEBUG`
  - `CURL_VERSION_TLSAUTH_SRP`
  - `CURL_VERSION_NTLM_WB`
  - `CURL_VERSION_HTTP2`
  - `CURL_VERSION_GSSAPI`
  - `CURLPAUSE_RECV`
  - `CURLPAUSE_RECV_CONT`
  - `CURLPAUSE_SEND`
  - `CURLPAUSE_SEND_CONT`
  - `CURLPAUSE_ALL`
  - `CURLPAUSE_CONT`
  - `curl_easy_setopt`
  - `curl_easy_getinfo`
  - `curl_share_setopt`
  - `curl_multi_setopt`

### compat/curl-for-windows/curl/include/curl/curlbuild.h
- Macros: __CURL_CURLBUILD_H, CURL_SIZEOF_LONG, CURL_TYPEOF_CURL_SOCKLEN_T, CURL_SIZEOF_CURL_SOCKLEN_T, CURL_TYPEOF_CURL_OFF_T, CURL_FORMAT_CURL_OFF_T, CURL_FORMAT_CURL_OFF_TU, CURL_FORMAT_OFF_T, CURL_SIZEOF_CURL_OFF_T, CURL_SUFFIX_CURL_OFF_T, CURL_SUFFIX_CURL_OFF_TU

### compat/curl-for-windows/curl/include/curl/curlrules.h
- Macros: __CURL_CURLRULES_H, CurlchkszEQ, CurlchkszGE, CURL_ISOCPP, __CURL_OFF_T_C_HLPR2, __CURL_OFF_T_C_HLPR1, CURL_OFF_T_C, CURL_OFF_TU_C

### compat/curl-for-windows/curl/include/curl/curlver.h
- Macros: __CURL_CURLVER_H, LIBCURL_COPYRIGHT, LIBCURL_VERSION, LIBCURL_VERSION_MAJOR, LIBCURL_VERSION_MINOR, LIBCURL_VERSION_PATCH, LIBCURL_VERSION_NUM, LIBCURL_TIMESTAMP

### compat/curl-for-windows/curl/include/curl/easy.h
- Functions: curl_easy_setopt, curl_easy_perform, curl_easy_cleanup, curl_easy_getinfo, curl_easy_duphandle, curl_easy_reset, curl_easy_recv, curl_easy_send
- Macros: __CURL_EASY_H

### compat/curl-for-windows/curl/include/curl/mprintf.h
- Functions: curl_mprintf, curl_mfprintf, curl_msprintf, curl_msnprintf, curl_mvprintf, curl_mvfprintf, curl_mvsprintf, curl_mvsnprintf
- Macros: __CURL_MPRINTF_H, printf, fprintf, sprintf, vsprintf, snprintf, vprintf, vfprintf, vsnprintf, aprintf, vaprintf

### compat/curl-for-windows/curl/include/curl/multi.h
- Functions: curl_multi_add_handle, curl_multi_remove_handle, curl_multi_fdset, curl_multi_wait, curl_multi_perform, curl_multi_cleanup, int, curl_multi_socket, curl_multi_socket_action, curl_multi_socket_all, curl_multi_setopt, curl_multi_assign
- Types: CURLMsg, curl_waitfd, each, is
- Macros: __CURL_MULTI_H, CURLM_CALL_MULTI_SOCKET, CURL_WAIT_POLLIN, CURL_WAIT_POLLPRI, CURL_WAIT_POLLOUT, CURL_POLL_NONE, CURL_POLL_IN, CURL_POLL_OUT, CURL_POLL_INOUT, CURL_POLL_REMOVE, CURL_SOCKET_TIMEOUT, CURL_CSELECT_IN, CURL_CSELECT_OUT, CURL_CSELECT_ERR, curl_multi_socket, CINIT, LONG, OBJECTPOINT, FUNCTIONPOINT, OFF_T

### compat/curl-for-windows/curl/include/curl/stdcheaders.h
- Functions: fread, fwrite, strcasecmp, strncasecmp
- Macros: __STDC_HEADERS_H

### compat/curl-for-windows/curl/include/curl/typecheck-gcc.h
- Functions: __attribute__, size_t, curlioerr, int, curl_socket_t, CURLcode
- Types: curl_httppost, curl_slist, curl_sockaddr
- Macros:
  - `__CURL_TYPECHECK_GCC_H`
  - `curl_easy_setopt`
  - `curl_easy_getinfo`
  - `curl_share_setopt`
  - `curl_multi_setopt`
  - `_CURL_WARNING`
  - `_curl_is_long_option`
  - `_curl_is_off_t_option`
  - `_curl_is_string_option`
  - `_curl_is_write_cb_option`
  - `_curl_is_conv_cb_option`
  - `_curl_is_cb_data_option`
  - `_curl_is_postfields_option`
  - `_curl_is_slist_option`
  - `_curl_is_string_info`
  - `_curl_is_long_info`
  - `_curl_is_double_info`
  - `_curl_is_slist_info`
  - `_curl_is_any_ptr`
  - `_curl_is_NULL`
  - `_curl_is_ptr`
  - `_curl_is_arr`
  - `_curl_is_string`
  - `_curl_is_long`
  - `_curl_is_off_t`
  - `_curl_is_error_buffer`
  - `_curl_is_cb_data`
  - `_curl_is_FILE`
  - `_curl_is_postfields`
  - `_curl_callback_compatible`
  - `_curl_is_read_cb`
  - `_curl_is_write_cb`
  - `_curl_is_ioctl_cb`
  - `_curl_is_sockopt_cb`
  - `_curl_is_opensocket_cb`
  - `_curl_is_progress_cb`
  - `_curl_is_debug_cb`
  - `_curl_is_ssl_ctx_cb`
  - `_curl_is_conv_cb`
  - `_curl_is_seek_cb`

### compat/curl-for-windows/openssl/config/opensslconf.h
- Macros:
  - `OPENSSL_SYSNAME_WIN32`
  - `OPENSSL_NO_CAPIENG`
  - `OPENSSL_NO_EC_NISTP_64_GCC_128`
  - `OPENSSL_NO_GMP`
  - `OPENSSL_NO_GOST`
  - `OPENSSL_NO_HW_PADLOCK`
  - `OPENSSL_NO_JPAKE`
  - `OPENSSL_NO_KRB5`
  - `OPENSSL_NO_MD2`
  - `OPENSSL_NO_RC5`
  - `OPENSSL_NO_RFC3779`
  - `OPENSSL_NO_SCTP`
  - `OPENSSL_NO_STORE`
  - `OPENSSL_THREADS`
  - `OPENSSL_NO_DYNAMIC_ENGINE`
  - `NO_CAMELLIA`
  - `NO_CAPIENG`
  - `NO_CAST`
  - `NO_CMS`
  - `NO_FIPS`
  - `NO_GMP`
  - `NO_IDEA`
  - `NO_JPAKE`
  - `NO_KRB5`
  - `NO_MD2`
  - `NO_MDC2`
  - `NO_RC5`
  - `NO_RFC3779`
  - `NO_SEED`
  - `NO_SHA0`
  - `NO_STORE`
  - `NO_WHRLPOOL`
  - `OPENSSL_FIPS`
  - `ENGINESDIR`
  - `OPENSSLDIR`
  - `OPENSSL_UNISTD`
  - `OPENSSL_EXPORT_VAR_AS_FUNCTION`
  - `IDEA_INT`
  - `MD2_INT`
  - `RC2_INT`
  - `RC4_INT`
  - `RC4_CHUNK`
  - `DES_LONG`
  - `CONFIG_HEADER_BN_H`
  - `BL_LLONG`
  - `SIXTY_FOUR_BIT`
  - `SIXTY_FOUR_BIT_LONG`
  - `THIRTY_TWO_BIT`
  - `CONFIG_HEADER_RC4_LOCL_H`
  - `RC4_INDEX`
  - `CONFIG_HEADER_BF_LOCL_H`
  - `BF_PTR`
  - `CONFIG_HEADER_DES_LOCL_H`
  - `DES_PTR`
  - `DES_RISC1`
  - `DES_UNROLL`
  - `DES_RISC2`

### compat/curl-for-windows/openssl/openssl/crypto/opensslconf.h
- No exported symbols detected; file provides local implementation details.

### compat/curl-for-windows/openssl/openssl/crypto/sha/sha.h
- Functions: private_SHA_Init, SHA_Init, SHA_Update, SHA_Final, SHA_Transform, private_SHA1_Init, SHA1_Init, SHA1_Update, SHA1_Final, SHA1_Transform, private_SHA224_Init, private_SHA256_Init, SHA224_Init, SHA224_Update, SHA224_Final, SHA256_Init, SHA256_Update, SHA256_Final, SHA256_Transform, private_SHA384_Init, private_SHA512_Init, SHA384_Init, SHA384_Update, SHA384_Final, SHA512_Init, SHA512_Update, SHA512_Final, SHA512_Transform
- Types: SHAstate_st, SHA256state_st, SHA512state_st
- Macros: HEADER_SHA_H, FIPS_SHA_SIZE_T, SHA_LONG, SHA_LONG_LOG2, SHA_LBLOCK, SHA_CBLOCK, SHA_LAST_BLOCK, SHA_DIGEST_LENGTH, SHA256_CBLOCK, SHA224_DIGEST_LENGTH, SHA256_DIGEST_LENGTH, SHA384_DIGEST_LENGTH, SHA512_DIGEST_LENGTH, SHA512_CBLOCK, SHA_LONG64, U64

### compat/curl-for-windows/openssl/openssl/e_os2.h
- Macros:
  - `HEADER_E_OS2_H`
  - `OPENSSL_SYS_UNIX`
  - `OPENSSL_SYS_MACINTOSH_CLASSIC`
  - `OPENSSL_SYS_NETWARE`
  - `OPENSSL_SYS_MSDOS`
  - `OPENSSL_SYS_WIN32_UWIN`
  - `OPENSSL_SYS_WIN32_CYGWIN`
  - `OPENSSL_SYS_WIN32`
  - `OPENSSL_SYS_WINNT`
  - `OPENSSL_SYS_WINCE`
  - `OPENSSL_SYS_WINDOWS`
  - `OPENSSL_OPT_WINDLL`
  - `OPENSSL_SYS_VMS`
  - `OPENSSL_SYS_VMS_DECC`
  - `OPENSSL_SYS_VMS_DECCXX`
  - `OPENSSL_SYS_VMS_NODECC`
  - `OPENSSL_SYS_OS2`
  - `OPENSSL_SYS_LINUX`
  - `OPENSSL_SYS_MPE`
  - `OPENSSL_SYS_SNI`
  - `OPENSSL_SYS_ULTRASPARC`
  - `OPENSSL_SYS_NEWS4`
  - `OPENSSL_SYS_MACOSX`
  - `OPENSSL_SYS_MACOSX_RHAPSODY`
  - `OPENSSL_SYS_SUNOS`
  - `OPENSSL_SYS_CRAY`
  - `OPENSSL_SYS_AIX`
  - `OPENSSL_SYS_VOS`
  - `OPENSSL_SYS_VOS_HPPA`
  - `OPENSSL_SYS_VOS_IA32`
  - `OPENSSL_SYS_VXWORKS`
  - `OPENSSL_SYS_BEOS`
  - `OPENSSL_SYS_BEOS_BONE`
  - `OPENSSL_SYS_BEOS_R5`
  - `OPENSSL_UNISTD_IO`
  - `OPENSSL_DECLARE_EXIT`
  - `OPENSSL_EXTERN`
  - `OPENSSL_EXPORT`
  - `OPENSSL_IMPORT`
  - `OPENSSL_GLOBAL`
  - `foobar`
  - `OPENSSL_IMPLEMENT_GLOBAL`
  - `OPENSSL_DECLARE_GLOBAL`
  - `OPENSSL_GLOBAL_REF`
  - `ossl_ssize_t`
  - `ssize_t`

### compat/curl-for-windows/openssl/openssl/include/openssl/e_os2.h
- No exported symbols detected; file provides local implementation details.

### compat/curl-for-windows/openssl/openssl/include/openssl/opensslconf.h
- No exported symbols detected; file provides local implementation details.

### compat/curl-for-windows/openssl/openssl/include/openssl/sha.h
- No exported symbols detected; file provides local implementation details.

### compat/curl-for-windows/zlib/zconf.h
- Macros:
  - `ZCONF_H`
  - `Z_PREFIX_SET`
  - `_dist_code`
  - `_length_code`
  - `_tr_align`
  - `_tr_flush_bits`
  - `_tr_flush_block`
  - `_tr_init`
  - `_tr_stored_block`
  - `_tr_tally`
  - `adler32`
  - `adler32_combine`
  - `adler32_combine64`
  - `compress`
  - `compress2`
  - `compressBound`
  - `crc32`
  - `crc32_combine`
  - `crc32_combine64`
  - `deflate`
  - `deflateBound`
  - `deflateCopy`
  - `deflateEnd`
  - `deflateInit2_`
  - `deflateInit_`
  - `deflateParams`
  - `deflatePending`
  - `deflatePrime`
  - `deflateReset`
  - `deflateResetKeep`
  - `deflateSetDictionary`
  - `deflateSetHeader`
  - `deflateTune`
  - `deflate_copyright`
  - `get_crc_table`
  - `gz_error`
  - `gz_intmax`
  - `gz_strwinerror`
  - `gzbuffer`
  - `gzclearerr`
  - `gzclose`
  - `gzclose_r`
  - `gzclose_w`
  - `gzdirect`
  - `gzdopen`
  - `gzeof`
  - `gzerror`
  - `gzflush`
  - `gzgetc`
  - `gzgetc_`
  - `gzgets`
  - `gzoffset`
  - `gzoffset64`
  - `gzopen`
  - `gzopen64`
  - `gzopen_w`
  - `gzprintf`
  - `gzvprintf`
  - `gzputc`
  - `gzputs`
  - `gzread`
  - `gzrewind`
  - `gzseek`
  - `gzseek64`
  - `gzsetparams`
  - `gztell`
  - `gztell64`
  - `gzungetc`
  - `gzwrite`
  - `inflate`
  - `inflateBack`
  - `inflateBackEnd`
  - `inflateBackInit_`
  - `inflateCopy`
  - `inflateEnd`
  - `inflateGetHeader`
  - `inflateInit2_`
  - `inflateInit_`
  - `inflateMark`
  - `inflatePrime`
  - `inflateReset`
  - `inflateReset2`
  - `inflateSetDictionary`
  - `inflateGetDictionary`
  - `inflateSync`
  - `inflateSyncPoint`
  - `inflateUndermine`
  - `inflateResetKeep`
  - `inflate_copyright`
  - `inflate_fast`
  - `inflate_table`
  - `uncompress`
  - `zError`
  - `zcalloc`
  - `zcfree`
  - `zlibCompileFlags`
  - `zlibVersion`
  - `Byte`
  - `Bytef`
  - `alloc_func`
  - `charf`
  - `free_func`
  - `gzFile`
  - `gz_header`
  - `gz_headerp`
  - `in_func`
  - `intf`
  - `out_func`
  - `uInt`
  - `uIntf`
  - `uLong`
  - `uLongf`
  - `voidp`
  - `voidpc`
  - `voidpf`
  - `gz_header_s`
  - `internal_state`
  - `MSDOS`
  - `OS2`
  - `WINDOWS`
  - `WIN32`
  - `SYS16BIT`
  - `MAXSEG_64K`
  - `UNALIGNED_OK`
  - `STDC`
  - `STDC99`
  - `const`
  - `z_const`
  - `NO_DUMMY_DECL`
  - `MAX_MEM_LEVEL`
  - `MAX_WBITS`
  - `OF`
  - `Z_ARG`
  - `SMALL_MEDIUM`
  - `FAR`
  - `ZEXTERN`
  - `ZEXPORT`
  - `ZEXPORTVA`
  - `Z_U4`
  - `Z_HAVE_UNISTD_H`
  - `Z_HAVE_STDARG_H`
  - `z_off_t`
  - `Z_LFS64`
  - `Z_LARGE64`
  - `Z_WANT64`
  - `SEEK_SET`
  - `SEEK_CUR`
  - `SEEK_END`
  - `z_off64_t`

### compat/curl-for-windows/zlib/zlib.h
- Functions: method, void, OF, compression, space, string, inflate, inflateInit2, caller, invalid, inconsistent, level, deflate, deflateInit2, size, dictionary, point, code, inflateBack, int, inflateBackInit, content, decompression, ignored, Z_ARG, gzbuffer, gzseek, gzdopen, true, the, gzclose, type
- Types: internal_state, z_stream_s, gz_header_s, gzFile_s
- Macros:
  - `ZLIB_H`
  - `ZLIB_VERSION`
  - `ZLIB_VERNUM`
  - `ZLIB_VER_MAJOR`
  - `ZLIB_VER_MINOR`
  - `ZLIB_VER_REVISION`
  - `ZLIB_VER_SUBREVISION`
  - `Z_NO_FLUSH`
  - `Z_PARTIAL_FLUSH`
  - `Z_SYNC_FLUSH`
  - `Z_FULL_FLUSH`
  - `Z_FINISH`
  - `Z_BLOCK`
  - `Z_TREES`
  - `Z_OK`
  - `Z_STREAM_END`
  - `Z_NEED_DICT`
  - `Z_ERRNO`
  - `Z_STREAM_ERROR`
  - `Z_DATA_ERROR`
  - `Z_MEM_ERROR`
  - `Z_BUF_ERROR`
  - `Z_VERSION_ERROR`
  - `Z_NO_COMPRESSION`
  - `Z_BEST_SPEED`
  - `Z_BEST_COMPRESSION`
  - `Z_DEFAULT_COMPRESSION`
  - `Z_FILTERED`
  - `Z_HUFFMAN_ONLY`
  - `Z_RLE`
  - `Z_FIXED`
  - `Z_DEFAULT_STRATEGY`
  - `Z_BINARY`
  - `Z_TEXT`
  - `Z_ASCII`
  - `Z_UNKNOWN`
  - `Z_DEFLATED`
  - `Z_NULL`
  - `zlib_version`
  - `deflateInit`
  - `inflateInit`
  - `deflateInit2`
  - `inflateInit2`
  - `inflateBackInit`
  - `z_gzgetc`
  - `gzgetc`
  - `z_gzopen`
  - `z_gzseek`
  - `z_gztell`
  - `z_gzoffset`
  - `z_adler32_combine`
  - `z_crc32_combine`
  - `gzopen`
  - `gzseek`
  - `gztell`
  - `gzoffset`
  - `adler32_combine`
  - `crc32_combine`

### compat/getopt/getopt.h
- Functions: getopt_long, getopt_long_only, getopt, getsubopt
- Types: option
- Macros: _GETOPT_H_, no_argument, required_argument, optional_argument, _GETOPT_DEFINED

### compat/getopt/getopt_long.c
- Functions: warnx, getopt_internal, parse_long_options, gcd, permute_args, getopt, getopt_long, getopt_long_only
- Types: option
- Macros: REPLACE_GETOPT, PRINT_ERROR, FLAG_PERMUTE, FLAG_ALLARGS, FLAG_LONGONLY, BADCH, BADARG, INORDER, EMSG

### compat/gettimeofday.c
- Functions: gettimeofday, usleep
- Types: timezone, timeval
- Macros: DELTA_EPOCH_IN_MICROSECS

### compat/inttypes.h
- No exported symbols detected; file provides local implementation details.

### compat/jansson/Makefile.am
- Role: build/config source

### compat/jansson/Makefile.in
- Role: build/config source

### compat/jansson/config.h
- Macros: HAVE_CLOSE, HAVE_FCNTL_H, HAVE_GETPID, HAVE_GETTIMEOFDAY, HAVE_INTTYPES_H, HAVE_LOCALECONV, HAVE_LOCALE_H, HAVE_LONG_LONG_INT, HAVE_MEMORY_H, HAVE_OPEN, HAVE_READ, HAVE_SCHED_H, HAVE_STDINT_H, HAVE_STDLIB_H, HAVE_STRINGS_H, HAVE_STRING_H, HAVE_STRTOLL, HAVE_SYNC_BUILTINS, HAVE_SYS_PARAM_H, HAVE_SYS_STAT_H, HAVE_SYS_TIME_H, HAVE_SYS_TYPES_H, HAVE_UNISTD_H, LT_OBJDIR, PACKAGE, PACKAGE_BUGREPORT, PACKAGE_NAME, PACKAGE_STRING, PACKAGE_TARNAME, PACKAGE_URL, PACKAGE_VERSION, STDC_HEADERS, USE_URANDOM, USE_WINDOWS_CRYPTOAPI, VERSION, below

### compat/jansson/configure.ac
- Role: build/config source

### compat/jansson/dump.c
- Functions: dump_to_strbuffer, strbuffer_append_bytes, dump_to_file, dump_indent, dump, dump_string, object_key_compare_keys, strcmp, object_key_compare_serials, do_dump, json_dumpf, json_dump_callback, json_dump_file
- Types: object_key
- Macros: _GNU_SOURCE, MAX_INTEGER_STR_LENGTH, MAX_REAL_STR_LENGTH

### compat/jansson/error.c
- Functions: jsonp_error_init, jsonp_error_set_source, jsonp_error_set, jsonp_error_vset

### compat/jansson/hashtable.c
- Functions: hash_str, list_init, list_insert, list_remove, bucket_is_empty, insert_to_bucket, num_buckets, hashtable_do_del, hashtable_do_clear, hashtable_do_rehash, hashtable_init, hashtable_close, hashtable_set, hashtable_del, hashtable_clear, hashtable_iter_next, hashtable_iter_serial, hashtable_iter_set
- Types: hashtable_list, hashtable_pair, hashtable_bucket
- Macros: list_to_pair

### compat/jansson/hashtable.h
- Functions: hashtable_init, hashtable_close, hashtable_set, hashtable_del, hashtable_clear, hashtable_iter_serial, hashtable_iter_set
- Types: hashtable_list, hashtable_pair, hashtable_bucket, hashtable
- Macros: HASHTABLE_H, hashtable_key_to_iter

### compat/jansson/jansson.h
- Functions:
  - `json_delete`
  - `json_decref`
  - `json_object_size`
  - `json_object_set_new`
  - `json_object_set_new_nocheck`
  - `json_object_del`
  - `json_object_clear`
  - `json_object_update`
  - `json_object_update_existing`
  - `json_object_update_missing`
  - `json_object_iter_set_new`
  - `json_object_set`
  - `json_object_set_nocheck`
  - `json_object_iter_set`
  - `json_array_size`
  - `json_array_set_new`
  - `json_array_append_new`
  - `json_array_insert_new`
  - `json_array_remove`
  - `json_array_clear`
  - `json_array_extend`
  - `json_array_set`
  - `json_array_append`
  - `json_array_insert`
  - `json_integer_value`
  - `json_real_value`
  - `json_number_value`
  - `json_string_set`
  - `json_string_set_nocheck`
  - `json_integer_set`
  - `json_real_set`
  - `json_unpack`
  - `json_unpack_ex`
  - `json_vunpack_ex`
  - `json_equal`
  - `size_t`
  - `int`
  - `json_dumpf`
  - `json_dump_file`
  - `json_dump_callback`
  - `void`
  - `json_set_alloc_funcs`
- Types: json_t
- Macros:
  - `JANSSON_H`
  - `JANSSON_MAJOR_VERSION`
  - `JANSSON_MINOR_VERSION`
  - `JANSSON_MICRO_VERSION`
  - `JANSSON_VERSION`
  - `JANSSON_VERSION_HEX`
  - `JSON_INTEGER_FORMAT`
  - `json_typeof`
  - `json_is_object`
  - `json_is_array`
  - `json_is_string`
  - `json_is_integer`
  - `json_is_real`
  - `json_is_number`
  - `json_is_true`
  - `json_is_false`
  - `json_is_boolean`
  - `json_is_null`
  - `json_boolean`
  - `JSON_ERROR_TEXT_LENGTH`
  - `JSON_ERROR_SOURCE_LENGTH`
  - `json_object_foreach`
  - `json_array_foreach`
  - `JSON_VALIDATE_ONLY`
  - `JSON_STRICT`
  - `JSON_REJECT_DUPLICATES`
  - `JSON_DISABLE_EOF_CHECK`
  - `JSON_DECODE_ANY`
  - `JSON_DECODE_INT_AS_REAL`
  - `JSON_INDENT`
  - `JSON_COMPACT`
  - `JSON_ENSURE_ASCII`
  - `JSON_SORT_KEYS`
  - `JSON_PRESERVE_ORDER`
  - `JSON_ENCODE_ANY`
  - `JSON_ESCAPE_SLASH`

### compat/jansson/jansson_config.h
- Macros: JANSSON_CONFIG_H, inline, JSON_INLINE, JSON_INTEGER_IS_LONG_LONG, JSON_HAVE_LOCALECONV

### compat/jansson/jansson_private.h
- Functions: jsonp_error_init, jsonp_error_set_source, jsonp_error_set, jsonp_error_vset, jsonp_strtod, jsonp_dtostr, jsonp_malloc, jsonp_free
- Macros: JANSSON_PRIVATE_H, container_of, max, va_copy, json_to_object, json_to_array, json_to_string, json_to_real, json_to_integer, snprintf, vsnprintf

### compat/jansson/load.c
- Functions: fgetc, error_set, stream_init, stream_get, stream_unget, lex_get, lex_save, lex_get_save, lex_unget, lex_unget_unsave, lex_save_cached, decode_unicode_escape, assert, lex_scan_string, lex_scan_number, lex_scan, lex_init, lex_close, string_get, buffer_get, callback_get
- Macros: _GNU_SOURCE, STREAM_STATE_OK, STREAM_STATE_EOF, STREAM_STATE_ERROR, TOKEN_INVALID, TOKEN_EOF, TOKEN_STRING, TOKEN_INTEGER, TOKEN_REAL, TOKEN_TRUE, TOKEN_FALSE, TOKEN_NULL, l_isupper, l_islower, l_isalpha, l_isdigit, l_isxdigit, stream_to_lex, json_strtoint, MAX_BUF_LEN

### compat/jansson/memory.c
- Functions: jsonp_free, json_set_alloc_funcs

### compat/jansson/pack_unpack.c
- Functions: scanner_init, next_token, prev_token, set_error, pack_object, pack_array, json_null, va_arg, json_integer, json_real, json_incref, unpack, unpack_object, unpack_array, json_vunpack_ex, json_unpack_ex, json_unpack
- Macros: token, type_name

### compat/jansson/strbuffer.c
- Functions: strbuffer_init, strbuffer_close, strbuffer_clear, strbuffer_append, strbuffer_append_bytes, strbuffer_append_byte, strbuffer_pop
- Macros: _GNU_SOURCE, STRBUFFER_MIN_SIZE, STRBUFFER_FACTOR, STRBUFFER_SIZE_MAX

### compat/jansson/strbuffer.h
- Functions: strbuffer_init, strbuffer_close, strbuffer_clear, strbuffer_append, strbuffer_append_byte, strbuffer_append_bytes, strbuffer_pop
- Macros: STRBUFFER_H

### compat/jansson/strconv.c
- Functions: to_locale, from_locale, jsonp_strtod, jsonp_dtostr, exponents

### compat/jansson/utf.c
- Functions: utf8_encode, utf8_check_first, utf8_check_full, utf8_check_string

### compat/jansson/utf.h
- Functions: utf8_encode, utf8_check_first, utf8_check_full, utf8_check_string
- Macros: UTF_H

### compat/jansson/util.h
- Macros: UTIL_H, max

### compat/jansson/value.c
- Functions:
  - `isnan`
  - `isinf`
  - `json_init`
  - `json_delete_object`
  - `json_object_size`
  - `hashtable_get`
  - `json_object_set_new_nocheck`
  - `json_object_set_new`
  - `json_object_del`
  - `hashtable_del`
  - `json_object_clear`
  - `json_object_update`
  - `json_object_update_existing`
  - `json_object_update_missing`
  - `hashtable_iter`
  - `hashtable_iter_at`
  - `hashtable_iter_next`
  - `hashtable_iter_key`
  - `json_object_iter_set_new`
  - `hashtable_key_to_iter`
  - `json_object_equal`
  - `json_delete_array`
  - `json_array_size`
  - `json_array_set_new`
  - `array_move`
  - `array_copy`
  - `json_array_append_new`
  - `json_array_insert_new`
  - `json_array_remove`
  - `json_array_clear`
  - `json_array_extend`
  - `json_array_equal`
  - `json_string_nocheck`
  - `json_string_set_nocheck`
  - `json_string_set`
  - `json_delete_string`
  - `json_string_equal`
  - `json_integer_value`
  - `json_integer_set`
  - `json_delete_integer`
  - `json_integer_equal`
  - `json_integer`
  - `json_real_value`
  - `json_real_set`
  - `json_delete_real`
  - `json_real_equal`
  - `json_real`
  - `json_number_value`
  - `json_delete`
  - `json_equal`
  - `json_object_copy`
  - `json_array_copy`
  - `json_string_copy`
  - `json_integer_copy`
  - `json_real_copy`
  - `json_object_deep_copy`
  - `json_array_deep_copy`
- Macros: _GNU_SOURCE

### compat/pthreads/pthread.h
- Functions:
  - `void`
  - `execute`
  - `cleanup`
  - `pthread_attr_init`
  - `pthread_attr_destroy`
  - `pthread_attr_getdetachstate`
  - `pthread_attr_getstackaddr`
  - `pthread_attr_getstacksize`
  - `pthread_attr_setdetachstate`
  - `pthread_attr_setstackaddr`
  - `pthread_attr_setstacksize`
  - `pthread_attr_getschedparam`
  - `pthread_attr_setschedparam`
  - `pthread_attr_setschedpolicy`
  - `pthread_attr_getschedpolicy`
  - `pthread_attr_setinheritsched`
  - `pthread_attr_getinheritsched`
  - `pthread_attr_setscope`
  - `pthread_attr_getscope`
  - `pthread_create`
  - `pthread_detach`
  - `pthread_equal`
  - `pthread_exit`
  - `pthread_join`
  - `pthread_self`
  - `pthread_cancel`
  - `pthread_setcancelstate`
  - `pthread_setcanceltype`
  - `pthread_testcancel`
  - `pthread_once`
  - `ptw32_pop_cleanup`
  - `ptw32_push_cleanup`
  - `pthread_key_create`
  - `pthread_key_delete`
  - `pthread_setspecific`
  - `pthread_getspecific`
  - `pthread_mutexattr_init`
  - `pthread_mutexattr_destroy`
  - `pthread_mutexattr_getpshared`
  - `pthread_mutexattr_setpshared`
  - `pthread_mutexattr_settype`
  - `pthread_mutexattr_gettype`
  - `pthread_mutexattr_setrobust`
  - `pthread_mutexattr_getrobust`
  - `pthread_barrierattr_init`
  - `pthread_barrierattr_destroy`
  - `pthread_barrierattr_getpshared`
  - `pthread_barrierattr_setpshared`
  - `pthread_mutex_init`
  - `pthread_mutex_destroy`
  - `pthread_mutex_lock`
  - `pthread_mutex_timedlock`
  - `pthread_mutex_trylock`
  - `pthread_mutex_unlock`
  - `pthread_mutex_consistent`
  - `pthread_spin_init`
  - `pthread_spin_destroy`
  - `pthread_spin_lock`
  - `pthread_spin_trylock`
  - `pthread_spin_unlock`
  - `pthread_barrier_init`
  - `pthread_barrier_destroy`
  - `pthread_barrier_wait`
  - `pthread_condattr_init`
  - `pthread_condattr_destroy`
  - `pthread_condattr_getpshared`
  - `pthread_condattr_setpshared`
  - `pthread_cond_init`
  - `pthread_cond_destroy`
  - `pthread_cond_wait`
  - `pthread_cond_timedwait`
  - `pthread_cond_signal`
  - `pthread_cond_broadcast`
  - `pthread_setschedparam`
  - `pthread_getschedparam`
  - `pthread_setconcurrency`
  - `pthread_getconcurrency`
  - `pthread_rwlock_init`
  - `pthread_rwlock_destroy`
  - `pthread_rwlock_tryrdlock`
  - `pthread_rwlock_trywrlock`
  - `pthread_rwlock_rdlock`
  - `pthread_rwlock_timedrdlock`
  - `pthread_rwlock_wrlock`
  - `pthread_rwlock_timedwrlock`
  - `pthread_rwlock_unlock`
  - `pthread_rwlockattr_init`
  - `pthread_rwlockattr_destroy`
  - `pthread_rwlockattr_getpshared`
  - `pthread_rwlockattr_setpshared`
  - `pthread_kill`
  - `pthread_mutexattr_setkind_np`
  - `pthread_mutexattr_getkind_np`
  - `pthread_delay_np`
  - `pthread_num_processors_np`
  - `pthread_getunique_np`
  - `pthread_win32_process_attach_np`
  - `pthread_win32_process_detach_np`
  - `pthread_win32_thread_attach_np`
  - `pthread_win32_thread_detach_np`
  - `pthread_win32_test_features_np`
  - `pthread_timechange_handler_np`
  - `pthread_getw32threadhandle_np`
  - `pthread_getw32threadid_np`
  - `pthreadCancelableWait`
  - `pthreadCancelableTimedWait`
  - `_errno`
  - `ptw32_get_exception_services_code`
- Types: timespec, pthread_attr_t_, pthread_once_t_, pthread_key_t_, pthread_mutex_t_, pthread_mutexattr_t_, pthread_cond_t_, pthread_condattr_t_, pthread_rwlock_t_, pthread_rwlockattr_t_, pthread_spinlock_t_, pthread_barrier_t_, pthread_barrierattr_t_, ptw32_cleanup_t, sched_param, ptw32_features
- Macros:
  - `PTW32_STATIC_LIB`
  - `PTHREAD_H`
  - `PTW32_VERSION`
  - `PTW32_VERSION_STRING`
  - `__CLEANUP_C`
  - `PTW32_LEVEL`
  - `PTW32_LEVEL_MAX`
  - `HAVE_STRUCT_TIMESPEC`
  - `HAVE_SIGNAL_H`
  - `PTW32_INCLUDE_WINDOWS_H`
  - `NEED_ERRNO`
  - `NEED_SEM`
  - `HAVE_MODE_T`
  - `ENOTSUP`
  - `ETIMEDOUT`
  - `ENOSYS`
  - `EDEADLK`
  - `EOWNERDEAD`
  - `ENOTRECOVERABLE`
  - `PTW32__HANDLE_DEF`
  - `HANDLE`
  - `PTW32__DWORD_DEF`
  - `DWORD`
  - `_TIMESPEC_DEFINED`
  - `SIG_BLOCK`
  - `SIG_UNBLOCK`
  - `SIG_SETMASK`
  - `_POSIX_THREADS`
  - `_POSIX_READER_WRITER_LOCKS`
  - `_POSIX_SPIN_LOCKS`
  - `_POSIX_BARRIERS`
  - `_POSIX_THREAD_SAFE_FUNCTIONS`
  - `_POSIX_THREAD_ATTR_STACKSIZE`
  - `_POSIX_THREAD_ATTR_STACKADDR`
  - `_POSIX_THREAD_PRIO_INHERIT`
  - `_POSIX_THREAD_PRIO_PROTECT`
  - `_POSIX_THREAD_PRIORITY_SCHEDULING`
  - `_POSIX_THREAD_PROCESS_SHARED`
  - `_POSIX_THREAD_DESTRUCTOR_ITERATIONS`
  - `PTHREAD_DESTRUCTOR_ITERATIONS`
  - `_POSIX_THREAD_KEYS_MAX`
  - `PTHREAD_KEYS_MAX`
  - `PTHREAD_STACK_MIN`
  - `_POSIX_THREAD_THREADS_MAX`
  - `PTHREAD_THREADS_MAX`
  - `_POSIX_SEM_NSEMS_MAX`
  - `SEM_NSEMS_MAX`
  - `_POSIX_SEM_VALUE_MAX`
  - `SEM_VALUE_MAX`
  - `PTW32_DLLPORT`
  - `PTW32_CDECL`
  - `PTHREAD_CANCELED`
  - `PTHREAD_ONCE_INIT`
  - `PTHREAD_MUTEX_INITIALIZER`
  - `PTHREAD_RECURSIVE_MUTEX_INITIALIZER`
  - `PTHREAD_ERRORCHECK_MUTEX_INITIALIZER`
  - `PTHREAD_RECURSIVE_MUTEX_INITIALIZER_NP`
  - `PTHREAD_ERRORCHECK_MUTEX_INITIALIZER_NP`
  - `PTHREAD_COND_INITIALIZER`
  - `PTHREAD_RWLOCK_INITIALIZER`
  - `PTHREAD_SPINLOCK_INITIALIZER`
  - `pthread_cleanup_push`
  - `pthread_cleanup_pop`
  - `errno`
  - `_ftime`
  - `_timeb`
  - `__except`
  - `PtW32CatchAll`
  - `catch`

### compat/pthreads/sched.h
- Functions: sched_yield, sched_get_priority_min, sched_get_priority_max, sched_setscheduler, sched_getscheduler
- Types: sched_param
- Macros: _SCHED_H, PTW32_SCHED_LEVEL, PTW32_SCHED_LEVEL_MAX, PTW32_DLLPORT, NEED_ERRNO, NEED_SEM, HAVE_STRUCT_TIMESPEC, HAVE_MODE_T, sched_rr_get_interval

### compat/stdbool.h
- Macros: false, true, bool

### compat/sys/time.h
- Functions: gettimeofday, usleep
- Types: timeval, timezone

### compat/unistd.h
- No exported symbols detected; file provides local implementation details.

### compat/winansi.c
- Functions: init, write_console, set_console_attr, erase_in_line, ansi_emulate, winansi_fputs, fputs, winansi_vfprintf, winansi_fprintf, winansi_printf
- Macros: FOREGROUND_ALL, BACKGROUND_ALL

### compat/winansi.h
- Functions: winansi_fputs, winansi_printf, winansi_fprintf, winansi_vfprintf
- Macros: isatty, fileno, fputs, printf, fprintf, vfprintf

### configure
- Role: build/config source

### configure.ac
- Role: build/config source

### cpu-miner.c
- Functions:
  - `ConsoleHandler`
  - `workio_cmd_free`
  - `drop_policy`
  - `affine_to_cpu_mask`
  - `SetThreadAffinityMask`
  - `get_currentalgo`
  - `snprintf`
  - `proper_exit`
  - `work_free`
  - `work_copy`
  - `calc_network_diff`
  - `work_decode`
  - `rpc2_job_decode`
  - `sprintf`
  - `get_mininginfo`
  - `gbt_work_decode`
  - `share_result`
  - `submit_upstream_work`
  - `get_upstream_work`
  - `workio_get_work`
  - `workio_submit_work`
  - `rpc2_login`
  - `rpc2_workio_login`
  - `get_work`
  - `submit_work`
  - `stratum_gen_work`
  - `sha256d`
  - `rpc2_stratum_job`
  - `wanna_mine`
  - `restart_threads`
  - `stratum_handle_response`
  - `applog`
  - `show_version_and_exit`
  - `show_usage_and_exit`
  - `printf`
  - `strhide`
  - `parse_arg`
  - `fprintf`
  - `parse_config`
  - `parse_cmdline`
  - `signal_handler`
  - `thread_create`
  - `show_credits`
  - `get_defconfig_path`
  - `main`
- Types: workio_commands, workio_cmd, thr_info, work, algos, work_restart, stratum_ctx, option, sched_param, not, timeval
- Macros: _GNU_SOURCE, LP_SCANTIME, min, max, pthread_setaffinity_np, POK_BOOL_MASK, POK_DATA_MASK, BLOCK_VERSION_CURRENT, YES, YAY, BOO, GBT_CAPABILITIES

### cpuminer-config.h
- Macros: HAVE_ALLOCA, HAVE_ALLOCA_H, HAVE_DECL_BE32DEC, HAVE_DECL_BE32ENC, HAVE_DECL_LE16DEC, HAVE_DECL_LE16ENC, HAVE_DECL_LE32DEC, HAVE_DECL_LE32ENC, HAVE_GETOPT_LONG, HAVE_INTTYPES_H, HAVE_LIBZ, HAVE_STDINT_H, HAVE_STDIO_H, HAVE_STDLIB_H, HAVE_STRINGS_H, HAVE_STRING_H, HAVE_SYSLOG_H, HAVE_SYS_PARAM_H, HAVE_SYS_STAT_H, HAVE_SYS_TYPES_H, HAVE_UNISTD_H, PACKAGE, PACKAGE_BUGREPORT, PACKAGE_NAME, PACKAGE_STRING, PACKAGE_TARNAME, PACKAGE_URL, PACKAGE_VERSION, STDC_HEADERS, USE_ASM, USE_AVX, USE_AVX2, USE_INT128, USE_XOP, VERSION

### cpuminer-config.h.in
- Role: build/config source

### crypto/aesb.c
- Functions: aesb_single_round, aesb_pseudo_round_mut
- Macros: TABLE_ALIGN, WPOLY, N_COLS, AES_BLOCK_SIZE, RC_LENGTH, ALIGN, rf1, word_in, word_out, s, si, so, state_in, state_out, round, to_byte, bval, fwd_var, fwd_rnd, sb_data, rc_data, bytes2word, h0, w0, w1, w2, w3, u0, u1, u2, u3, v0, v1, v2, v3, f2, f4, f8, f3, f9, fb, fd, fe, t_dec, t_set, t_use, d_4, four_tables

### crypto/blake2b.c
- Functions: blake2b_compress, blake2b_init, blake2b_final
- Macros: ROTR64, B2B_GET64, B2B_G

### crypto/blake2b.h
- Functions: blake2b_init, blake2b_update, blake2b_final
- Macros: __BLAKE2B_H__, inline, ALIGN, NATIVE_LITTLE_ENDIAN

### crypto/blake2s.c
- Functions: blake2s_set_lastnode, blake2s_clear_lastnode, blake2s_set_lastblock, blake2s_clear_lastblock, blake2s_increment_counter, blake2s_param_set_digest_length, blake2s_param_set_fanout, blake2s_param_set_max_depth, blake2s_param_set_leaf_length, blake2s_param_set_node_offset, blake2s_param_set_node_depth, blake2s_param_set_inner_length, blake2s_param_set_salt, blake2s_param_set_personal, blake2s_init0, blake2s_init_param, blake2s_init, blake2s_init_key, blake2s_compress, blake2s_update, blake2s_final, blake2s, main
- Macros: G, ROUND

### crypto/blake2s.h
- Functions: load32, store32, load48, store48, secure_zero_memory, blake2s_compress, blake2s_init, blake2s_init_key, blake2s_init_param, blake2s_update, blake2s_final, blake2s
- Types: blake2s_constant, __blake2s_param, __blake2s_state
- Macros: __BLAKE2_H__, inline, ALIGN, NATIVE_LITTLE_ENDIAN, blake2s_salt32, blake2s_simple

### crypto/c_blake256.c
- Functions: blake256_compress, blake256_init, blake224_init, blake256_update, blake224_update, blake256_final_h, blake256_final, blake224_final, blake256_hash, blake224_hash, hmac_blake256_init, hmac_blake224_init, hmac_blake256_update, hmac_blake224_update, hmac_blake256_final, hmac_blake224_final, hmac_blake256_hash, hmac_blake224_hash
- Macros: U8TO32, U32TO8, ROT, G

### crypto/c_blake256.h
- Functions: blake256_init, blake224_init, blake256_update, blake224_update, blake256_final, blake224_final, blake256_hash, blake224_hash, hmac_blake256_init, hmac_blake224_init, hmac_blake256_update, hmac_blake224_update, hmac_blake256_final, hmac_blake224_final, hmac_blake256_hash, hmac_blake224_hash
- Macros: _BLAKE256_H_

### crypto/c_groestl.c
- Functions: RND512P, RND512Q, F512, Transform, OutputTransformation, Init, Update, Final, groestl, crypto_hash
- Macros: P_TYPE, Q_TYPE, ROTATE_COLUMN_DOWN, COLUMN, BILB

### crypto/c_groestl.h
- Functions: Update, Final, groestl, crypto_hash
- Macros: __hash_h, ROWS, LENGTHFIELDLEN, COLS512, SIZE512, ROUNDS512, HASH_BIT_LEN, ROTL32, li_32, EXT_BYTE, u32BIG

### crypto/c_jh.c
- Functions: E8, F8, Init, Update, Final, jh_hash, memcpy
- Macros: DATA_ALIGN16, SWAP1, SWAP2, SWAP4, SWAP8, SWAP16, SWAP32, L, SS

### crypto/c_jh.h
- Functions: jh_hash

### crypto/c_keccak.c
- Functions: keccakf, keccak, keccak1600

### crypto/c_keccak.h
- Functions: keccak, keccakf, keccak1600
- Macros: KECCAK_H, KECCAK_ROUNDS, ROTL64

### crypto/c_skein.c
- Functions:
  - `Skein_256_Init`
  - `Skein_512_Init`
  - `Skein1024_Init`
  - `Skein_256_Update`
  - `Skein_512_Update`
  - `Skein1024_Update`
  - `Skein_256_Final`
  - `Skein_512_Final`
  - `Skein1024_Final`
  - `Skein_256_InitExt`
  - `Skein_512_InitExt`
  - `Skein1024_InitExt`
  - `Skein_256_Final_Pad`
  - `Skein_512_Final_Pad`
  - `Skein1024_Final_Pad`
  - `Skein_256_Output`
  - `Skein_512_Output`
  - `Skein1024_Output`
  - `Skein_256_Process_Block`
  - `Skein_256_Process_Block_CodeSize`
  - `Skein_256_Unroll_Cnt`
  - `Skein_512_Process_Block`
  - `Skein_512_Process_Block_CodeSize`
  - `Skein_512_Unroll_Cnt`
  - `Skein1024_Process_Block`
  - `Skein1024_Process_Block_CodeSize`
  - `Skein1024_Unroll_Cnt`
  - `Skein_256_API_CodeSize`
  - `Skein_512_API_CodeSize`
  - `Skein1024_API_CodeSize`
  - `Init`
  - `Update`
  - `Final`
  - `skein_hash`
- Macros:
  - `SKEIN_PORT_CODE`
  - `DISABLE_UNUSED`
  - `SKEIN_256_NIST_MAX_HASHBITS`
  - `SKEIN_512_NIST_MAX_HASHBITS`
  - `SKEIN_MODIFIER_WORDS`
  - `SKEIN_256_STATE_WORDS`
  - `SKEIN_512_STATE_WORDS`
  - `SKEIN1024_STATE_WORDS`
  - `SKEIN_MAX_STATE_WORDS`
  - `SKEIN_256_STATE_BYTES`
  - `SKEIN_512_STATE_BYTES`
  - `SKEIN1024_STATE_BYTES`
  - `SKEIN_256_STATE_BITS`
  - `SKEIN_512_STATE_BITS`
  - `SKEIN1024_STATE_BITS`
  - `SKEIN_256_BLOCK_BYTES`
  - `SKEIN_512_BLOCK_BYTES`
  - `SKEIN1024_BLOCK_BYTES`
  - `SKEIN_RND_SPECIAL`
  - `SKEIN_RND_KEY_INITIAL`
  - `SKEIN_RND_KEY_INJECT`
  - `SKEIN_RND_FEED_FWD`
  - `SKEIN_TREE_HASH`
  - `SKEIN_T1_BIT`
  - `SKEIN_T1_POS_TREE_LVL`
  - `SKEIN_T1_POS_BIT_PAD`
  - `SKEIN_T1_POS_BLK_TYPE`
  - `SKEIN_T1_POS_FIRST`
  - `SKEIN_T1_POS_FINAL`
  - `SKEIN_T1_FLAG_FIRST`
  - `SKEIN_T1_FLAG_FINAL`
  - `SKEIN_T1_FLAG_BIT_PAD`
  - `SKEIN_T1_TREE_LVL_MASK`
  - `SKEIN_T1_TREE_LEVEL`
  - `SKEIN_BLK_TYPE_KEY`
  - `SKEIN_BLK_TYPE_CFG`
  - `SKEIN_BLK_TYPE_PERS`
  - `SKEIN_BLK_TYPE_PK`
  - `SKEIN_BLK_TYPE_KDF`
  - `SKEIN_BLK_TYPE_NONCE`
  - `SKEIN_BLK_TYPE_MSG`
  - `SKEIN_BLK_TYPE_OUT`
  - `SKEIN_BLK_TYPE_MASK`
  - `SKEIN_T1_BLK_TYPE`
  - `SKEIN_T1_BLK_TYPE_KEY`
  - `SKEIN_T1_BLK_TYPE_CFG`
  - `SKEIN_T1_BLK_TYPE_PERS`
  - `SKEIN_T1_BLK_TYPE_PK`
  - `SKEIN_T1_BLK_TYPE_KDF`
  - `SKEIN_T1_BLK_TYPE_NONCE`
  - `SKEIN_T1_BLK_TYPE_MSG`
  - `SKEIN_T1_BLK_TYPE_OUT`
  - `SKEIN_T1_BLK_TYPE_MASK`
  - `SKEIN_T1_BLK_TYPE_CFG_FINAL`
  - `SKEIN_T1_BLK_TYPE_OUT_FINAL`
  - `SKEIN_VERSION`
  - `SKEIN_ID_STRING_LE`
  - `SKEIN_MK_64`
  - `SKEIN_SCHEMA_VER`
  - `SKEIN_KS_PARITY`
  - `SKEIN_CFG_STR_LEN`
  - `SKEIN_CFG_TREE_LEAF_SIZE_POS`
  - `SKEIN_CFG_TREE_NODE_SIZE_POS`
  - `SKEIN_CFG_TREE_MAX_LEVEL_POS`
  - `SKEIN_CFG_TREE_LEAF_SIZE_MSK`
  - `SKEIN_CFG_TREE_NODE_SIZE_MSK`
  - `SKEIN_CFG_TREE_MAX_LEVEL_MSK`
  - `SKEIN_CFG_TREE_INFO`
  - `SKEIN_CFG_TREE_INFO_SEQUENTIAL`
  - `Skein_Get_Tweak`
  - `Skein_Set_Tweak`
  - `Skein_Get_T0`
  - `Skein_Get_T1`
  - `Skein_Set_T0`
  - `Skein_Set_T1`
  - `Skein_Set_T0_T1`
  - `Skein_Set_Type`
  - `Skein_Start_New_Type`
  - `Skein_Clear_First_Flag`
  - `Skein_Set_Bit_Pad_Flag`
  - `Skein_Set_Tree_Level`
  - `Skein_Show_Block`
  - `Skein_Show_Round`
  - `Skein_Show_R_Ptr`
  - `Skein_Show_Final`
  - `Skein_Show_Key`
  - `Skein_Assert`
  - `Skein_assert`
  - `SKEIN_256_ROUNDS_TOTAL`
  - `SKEIN_512_ROUNDS_TOTAL`
  - `SKEIN1024_ROUNDS_TOTAL`
  - `MK_64`
  - `SKEIN_USE_ASM`
  - `SKEIN_LOOP`
  - `BLK_BITS`
  - `KW_TWK_BASE`
  - `KW_KEY_BASE`
  - `ks`
  - `ts`
  - `DebugSaveTweak`
  - `RCNT`
  - `SKEIN_UNROLL_256`
  - `Round256`
  - `R256`
  - `I256`
  - `R256_8_rounds`
  - `R256_Unroll_R`
  - `SKEIN_UNROLL_512`
  - `Round512`
  - `R512`
  - `I512`
  - `R512_8_rounds`
  - `R512_Unroll_R`
  - `SKEIN_UNROLL_1024`
  - `Round1024`
  - `R1024`
  - `I1024`
  - `R1024_8_rounds`
  - `R1024_Unroll_R`

### crypto/c_skein.h
- Functions: skein_hash
- Macros: _SKEIN_H_

### crypto/groestl_tables.h
- Macros: __tables_h

### crypto/hash-ops.h
- Functions: place_length, hash_permutation, hash_process, cn_fast_hash, cn_slow_hash, hash_extra_blake, hash_extra_groestl, hash_extra_jh, hash_extra_skein, tree_hash
- Types: hash_state

### crypto/hash.c
- Functions: hash_permutation, hash_process, cn_fast_hash
- Types: hash_state

### crypto/hash.h
- No exported symbols detected; file provides local implementation details.

### crypto/int-util.h
- Functions: rol32, _rotl, rol64, _rotl64, hi_dword, lo_dword, div_with_reminder, div128_32, ident32, ident64, swap32, swap64, mem_inplace_ident, mem_inplace_swap32, mem_inplace_swap64, memcpy_ident32, memcpy_ident64, memcpy_swap32, memcpy_swap64
- Macros: INT_UTILS_H_, inline, LITTLE_ENDIAN, BIG_ENDIAN, BYTE_ORDER, IDENT32, IDENT64, SWAP32, SWAP64, UNUSED, SWAP32LE, SWAP32BE, swap32le, swap32be, mem_inplace_swap32le, mem_inplace_swap32be, memcpy_swap32le, memcpy_swap32be, SWAP64LE, SWAP64BE, swap64le, swap64be, mem_inplace_swap64le, mem_inplace_swap64be, memcpy_swap64le, memcpy_swap64be

### crypto/oaes_config.h
- Macros: _OAES_CONFIG_H

### crypto/oaes_lib.c
- Functions: ftime, oaes_sub_byte, oaes_inv_sub_byte, oaes_word_rot_right, oaes_word_rot_left, oaes_shift_rows, oaes_inv_shift_rows, oaes_gf_mul, oaes_mix_cols, oaes_inv_mix_cols, oaes_sprintf, oaes_get_seed, oaes_key_destroy, oaes_key_expand, oaes_key_gen, oaes_key_gen_128, oaes_key_gen_192, oaes_key_gen_256, oaes_key_export, oaes_key_export_data, oaes_key_import, oaes_key_import_data, oaes_alloc, oaes_free, oaes_set_option, oaes_encrypt_block, oaes_decrypt_block, oaes_encrypt, oaes_decrypt, oaes_encryption_round, oaes_pseudo_encrypt_ecb
- Types: timeb, timezone, timeval, tm
- Macros: NO_OLDNAMES, getpid, OAES_RKEY_LEN, OAES_COL_LEN, OAES_ROUND_BASE, OAES_FLAG_PAD, min

### crypto/oaes_lib.h
- Functions: int, oaes_alloc, oaes_free, oaes_set_option, oaes_key_gen_128, oaes_key_gen_192, oaes_key_gen_256, oaes_key_export, oaes_key_export_data, oaes_key_import, oaes_key_import_data, oaes_encrypt, oaes_decrypt, oaes_sprintf, oaes_encryption_round, oaes_pseudo_encrypt_ecb
- Types: _oaes_key, _oaes_ctx
- Macros: _OAES_LIB_H, OAES_API, OAES_VERSION, OAES_BLOCK_SIZE, OAES_OPTION_NONE, OAES_OPTION_ECB, OAES_OPTION_CBC, OAES_OPTION_STEP_ON, OAES_OPTION_STEP_OFF

### crypto/skein_port.h
- Macros: _SKEIN_PORT_H_, RETURN_VALUES, VOID_RETURN, INT_RETURN, ui_type, dec_unit_type, dec_bufr_type, ptr_cast, RotL_64, IS_BIG_ENDIAN, IS_LITTLE_ENDIAN, PLATFORM_BYTE_ORDER, PLATFORM_MUST_ALIGN, SKEIN_NEED_SWAP, Skein_Put64_LSB_First, Skein_Get64_LSB_First, Skein_Swap64

### elist.h
- Functions: __list_add, list_add, list_add_tail, __list_del, list_del, list_del_init, list_move, list_move_tail, list_empty, __list_splice, list_splice, list_splice_init
- Types: list_head, for, this
- Macros: _LINUX_LIST_H, LIST_HEAD_INIT, LIST_HEAD, INIT_LIST_HEAD, list_entry, list_for_each, list_for_each_prev, list_for_each_safe, list_for_each_entry, list_for_each_entry_safe, list_for_each_entry_continue

### lyra2/Lyra2.c
- Functions: LYRA2, LYRA2_3

### lyra2/Lyra2.h
- Functions: LYRA2, LYRA2_3
- Macros: LYRA2_H_, BLOCK_LEN_BLAKE2_SAFE_INT64, BLOCK_LEN_BLAKE2_SAFE_BYTES, BLOCK_LEN_INT64, BLOCK_LEN_BYTES

### lyra2/Sponge.c
- Functions: initState, blake2bLyra, reducedBlake2bLyra, squeeze, absorbBlock, absorbBlockBlake2Safe, reducedSqueezeRow0, reducedDuplexRow1, reducedDuplexRowSetup, reducedDuplexRow, printArray

### lyra2/Sponge.h
- Functions: rotr64, _rotr64, initState, squeeze, reducedSqueezeRow0, absorbBlock, absorbBlockBlake2Safe, reducedDuplexRow1, reducedDuplexRowSetup, reducedDuplexRow, printArray
- Macros: SPONGE_H_, G, ROUND_LYRA

### miner.h
- Functions:
  - `is_windows`
  - `swab32`
  - `__builtin_bswap32`
  - `bswap_32`
  - `be32dec`
  - `le32dec`
  - `be32enc`
  - `le32enc`
  - `le16dec`
  - `le16enc`
  - `json_load_url`
  - `sha256_init`
  - `sha256_transform`
  - `sha256d`
  - `sha256_use_4way`
  - `sha256_init_4way`
  - `sha256_transform_4way`
  - `sha256_use_8way`
  - `sha256_init_8way`
  - `sha256_transform_8way`
  - `scanhash_allium`
  - `scanhash_axiom`
  - `scanhash_bastion`
  - `scanhash_blake`
  - `scanhash_blakecoin`
  - `scanhash_blake2b`
  - `scanhash_blake2s`
  - `scanhash_bmw`
  - `scanhash_cryptolight`
  - `scanhash_cryptonight`
  - `scanhash_c11`
  - `scanhash_decred`
  - `scanhash_drop`
  - `scanhash_fresh`
  - `scanhash_geek`
  - `scanhash_groestl`
  - `scanhash_heavy`
  - `scanhash_ink`
  - `scanhash_keccak`
  - `scanhash_jha`
  - `scanhash_lbry`
  - `scanhash_luffa`
  - `scanhash_lyra2`
  - `scanhash_lyra2rev2`
  - `scanhash_lyra2v3`
  - `scanhash_myriad`
  - `scanhash_neoscrypt`
  - `scanhash_nist5`
  - `scanhash_pentablake`
  - `scanhash_phi1612`
  - `scanhash_phi2`
  - `scanhash_pluck`
  - `scanhash_quark`
  - `init_quarkhash_contexts`
  - `scanhash_qubit`
  - `scanhash_rf256`
  - `scanhash_sha256d`
  - `scanhash_scrypt`
  - `scanhash_scryptjane`
  - `scanhash_sia`
  - `scanhash_sib`
  - `scanhash_skein`
  - `scanhash_skein2`
  - `scanhash_sonoa`
  - `scanhash_s3`
  - `scanhash_timetravel`
  - `scanhash_bitcore`
  - `scanhash_tribus`
  - `scanhash_veltor`
  - `scanhash_x11evo`
  - `scanhash_x11`
  - `scanhash_x12`
  - `scanhash_x13`
  - `scanhash_x14`
  - `scanhash_x15`
  - `scanhash_x16r`
  - `scanhash_x16rv2`
  - `scanhash_x16s`
  - `scanhash_x17`
  - `scanhash_x20r`
  - `scanhash_xevan`
  - `scanhash_yescrypt`
  - `scanhash_yescryptr8`
  - `scanhash_yescryptr16`
  - `scanhash_yescryptr32`
  - `scanhash_zr5`
  - `applog`
  - `restart_threads`
  - `bin2hex`
  - `hex2bin`
  - `jobj_binary`
  - `varint_encode`
  - `address_to_script`
  - `timeval_subtract`
  - `fulltest`
  - `work_set_target`
  - `target_to_diff`
  - `hash_target_ratio`
  - `work_set_target_ratio`
  - `get_currentalgo`
  - `has_aes_ni`
  - `cpu_bestfeature`
  - `cpu_getname`
  - `cpu_getmodelid`
  - `cpu_temp`
  - `stratum_socket_full`
  - `stratum_send_line`
  - `stratum_connect`
  - `stratum_disconnect`
  - `stratum_subscribe`
  - `stratum_authorize`
  - `stratum_handle_method`
  - `rpc2_login`
  - `rpc2_login_decode`
  - `rpc2_workio_login`
  - `rpc2_stratum_job`
  - `rpc2_job_decode`
  - `tq_free`
  - `tq_push`
  - `tq_freeze`
  - `tq_thaw`
  - `parse_arg`
  - `parse_config`
  - `proper_exit`
  - `applog_compare_hash`
  - `applog_hex`
  - `applog_hash`
  - `applog_hash64`
  - `format_hashrate`
  - `print_hash_tests`
  - `allium_hash`
  - `axiomhash`
  - `bastionhash`
  - `blakehash`
  - `blakecoinhash`
  - `blake2s_hash`
  - `blake2b_hash`
  - `bmwhash`
  - `c11hash`
  - `cryptolight_hash`
  - `cryptonight_hash`
  - `cryptonight_hash_v1`
  - `decred_hash`
  - `droplp_hash`
  - `groestlhash`
  - `heavyhash`
  - `quarkhash`
  - `freshhash`
  - `geekhash`
  - `keccakhash`
  - `inkhash`
  - `jha_hash`
  - `lbry_hash`
  - `luffahash`
  - `lyra2_hash`
  - `lyra2rev2_hash`
  - `lyra2v3_hash`
  - `myriadhash`
  - `neoscrypt`
  - `nist5hash`
  - `phi1612_hash`
  - `phi2_hash`
  - `pluck_hash`
  - `pentablakehash`
  - `qubithash`
  - `rf256_hash`
  - `scrypthash`
  - `scryptjanehash`
  - `sibhash`
  - `skeinhash`
  - `skein2hash`
  - `sonoa_hash`
  - `s3hash`
  - `timetravel_hash`
  - `bitcore_hash`
  - `tribus_hash`
  - `veltor_hash`
  - `xevan_hash`
  - `x11evo_hash`
  - `x11hash`
  - `x12hash`
  - `x13hash`
  - `x14hash`
  - `x15hash`
  - `x16r_hash`
  - `x16rv2_hash`
  - `x16s_hash`
  - `x17hash`
  - `x20r_hash`
  - `zr5hash`
  - `yescrypthash`
  - `yescrypt_hash_r8`
  - `yescrypt_hash_r16`
  - `yescrypt_hash_r32`
  - `zr5hash_pok`
- Types: work, cpu_info, thr_api, thread_q, thr_info, work_restart, timeval, stratum_job, stratum_ctx, timespec
- Macros: __MINER_H__, USER_AGENT, MAX_CPUS, __i386__, __x86_64__, alloca, LOG_BLUE, ARRAY_SIZE, WANT_BUILTIN_BSWAP, bswap_32, JSON_LOADS, JSON_LOADF, HAVE_SHA256_4WAY, HAVE_SHA256_8WAY, JSON_RPC_LONGPOLL, JSON_RPC_QUIET_404, JSON_RPC_IGNOREERR, JSON_BUF_LEN, CL_N, CL_RED, CL_GRN, CL_YLW, CL_BLU, CL_MAG, CL_CYN, CL_BLK, CL_RD2, CL_GR2, CL_BRW, CL_BL2, CL_MA2, CL_CY2, CL_SIL, CL_GRY, CL_LRD, CL_LGR, CL_YL2, CL_LBL, CL_LMA, CL_LCY, CL_WHT

### mingw64.sh
- Entry: script entrypoint

### nomacro.pl
- Entry: script entrypoint

### res/cpuminer.rc
- Role: build/config source

### res/icon.rc
- Role: build/config source

### res/resource.h
- No exported symbols detected; file provides local implementation details.

### scryptjane/scrypt-conf.h
- Macros: SCRYPT_CHOOSE_RUNTIME

### scryptjane/scrypt-jane-chacha.h
- Functions: scrypt_getROMix, available_implementations, scrypt_test_mix
- Macros: SCRYPT_MIX_BASE, SCRYPT_WORDTO8_LE, SCRYPT_WORD_ENDIAN_SWAP, SCRYPT_BLOCK_BYTES, SCRYPT_BLOCK_WORDS, SCRYPT_CHUNKMIX_FN, SCRYPT_CHUNKMIX_1_FN, SCRYPT_CHUNKMIX_1_XOR_FN, SCRYPT_ROMIX_FN, SCRYPT_MIX_FN, SCRYPT_ROMIX_TANGLE_FN, SCRYPT_ROMIX_UNTANGLE_FN

### scryptjane/scrypt-jane-hash.h
- Functions: scrypt_hash_init, scrypt_hash_update, scrypt_hash_finish, scrypt_test_hash, scrypt_verify
- Types: scrypt_hash_state_t
- Macros: SCRYPT_HASH, SCRYPT_HASH_BLOCK_SIZE, SCRYPT_HASH_DIGEST_SIZE, SCRYPT_TEST_HASH_LEN

### scryptjane/scrypt-jane-hash_blake256.h
- Functions: blake256_blocks, scrypt_hash_init, scrypt_hash_update, scrypt_hash_finish
- Types: scrypt_hash_state_t
- Macros: SCRYPT_HASH, SCRYPT_HASH_BLOCK_SIZE, SCRYPT_HASH_DIGEST_SIZE, G

### scryptjane/scrypt-jane-hash_blake512.h
- Functions: blake512_blocks, scrypt_hash_init, scrypt_hash_update, scrypt_hash_finish
- Types: scrypt_hash_state_t
- Macros: SCRYPT_HASH, SCRYPT_HASH_BLOCK_SIZE, SCRYPT_HASH_DIGEST_SIZE, G

### scryptjane/scrypt-jane-hash_keccak.h
- Functions: keccak_block, scrypt_hash_init, scrypt_hash_update, scrypt_hash_finish
- Types: scrypt_hash_state_t
- Macros: SCRYPT_HASH, SCRYPT_HASH_DIGEST_SIZE, SCRYPT_KECCAK_F, SCRYPT_KECCAK_C, SCRYPT_KECCAK_R, SCRYPT_HASH_BLOCK_SIZE

### scryptjane/scrypt-jane-hash_sha256.h
- Functions: sha256_blocks, scrypt_hash_init, scrypt_hash_update, scrypt_hash_finish
- Types: scrypt_hash_state_t
- Macros: SCRYPT_HASH, SCRYPT_HASH_BLOCK_SIZE, SCRYPT_HASH_DIGEST_SIZE, Ch, Maj, S0, S1, G0, G1, W0, W1, STEP

### scryptjane/scrypt-jane-hash_sha512.h
- Functions: sha512_blocks, scrypt_hash_init, scrypt_hash_update, scrypt_hash_finish
- Types: scrypt_hash_state_t
- Macros: SCRYPT_HASH, SCRYPT_HASH_BLOCK_SIZE, SCRYPT_HASH_DIGEST_SIZE, Ch, Maj, S0, S1, G0, G1, W0, W1, STEP

### scryptjane/scrypt-jane-hash_skein512.h
- Functions: skein512_blocks, scrypt_hash_init, scrypt_hash_update, scrypt_hash_finish
- Types: scrypt_hash_state_t
- Macros: SCRYPT_HASH, SCRYPT_HASH_BLOCK_SIZE, SCRYPT_HASH_DIGEST_SIZE

### scryptjane/scrypt-jane-mix_chacha-avx.h
- Functions: scrypt_ChunkMix_avx, scrypt_ChunkMix_avx_1, scrypt_ChunkMix_avx_1_xor
- Macros: SCRYPT_CHACHA_AVX, SCRYPT_MIX, SCRYPT_CHACHA_INCLUDED

### scryptjane/scrypt-jane-mix_chacha-sse2.h
- Functions: scrypt_ChunkMix_sse2, scrypt_ChunkMix_sse2_1, scrypt_ChunkMix_sse2_1_xor
- Macros: SCRYPT_CHACHA_SSE2, SCRYPT_MIX, SCRYPT_CHACHA_INCLUDED

### scryptjane/scrypt-jane-mix_chacha-ssse3.h
- Functions: scrypt_ChunkMix_ssse3, scrypt_ChunkMix_ssse3_1, scrypt_ChunkMix_ssse3_1_xor
- Macros: SCRYPT_CHACHA_SSSE3, SCRYPT_MIX, SCRYPT_CHACHA_INCLUDED

### scryptjane/scrypt-jane-mix_chacha.h
- Functions: chacha_core_basic
- Macros: SCRYPT_MIX, SCRYPT_CHACHA_INCLUDED, SCRYPT_CHACHA_BASIC, quarter

### scryptjane/scrypt-jane-mix_salsa-avx.h
- Functions: scrypt_ChunkMix_avx
- Macros: SCRYPT_SALSA_AVX, SCRYPT_MIX, SCRYPT_SALSA_INCLUDED

### scryptjane/scrypt-jane-mix_salsa-sse2.h
- Functions: scrypt_ChunkMix_sse2, salsa_core_tangle_sse2
- Macros: SCRYPT_SALSA_SSE2, SCRYPT_MIX, SCRYPT_SALSA_INCLUDED

### scryptjane/scrypt-jane-mix_salsa.h
- Functions: salsa_core_basic
- Macros: SCRYPT_MIX, SCRYPT_SALSA_INCLUDED, SCRYPT_SALSA_BASIC, quarter

### scryptjane/scrypt-jane-mix_salsa64-avx.h
- Functions: scrypt_ChunkMix_avx
- Macros: SCRYPT_SALSA64_AVX, SCRYPT_MIX, SCRYPT_SALSA64_INCLUDED

### scryptjane/scrypt-jane-mix_salsa64-sse2.h
- Functions: scrypt_ChunkMix_sse2, salsa64_core_tangle_sse2
- Macros: SCRYPT_SALSA64_SSE2, SCRYPT_MIX, SCRYPT_SALSA64_INCLUDED

### scryptjane/scrypt-jane-mix_salsa64-ssse3.h
- Functions: scrypt_ChunkMix_ssse3
- Macros: SCRYPT_SALSA64_SSSE3, SCRYPT_MIX, SCRYPT_SALSA64_INCLUDED

### scryptjane/scrypt-jane-mix_salsa64.h
- Functions: salsa64_core_basic
- Macros: SCRYPT_MIX, SCRYPT_SALSA64_INCLUDED, SCRYPT_SALSA64_BASIC, G

### scryptjane/scrypt-jane-pbkdf2.h
- Functions: scrypt_hash, scrypt_hmac_init, scrypt_hmac_update, scrypt_hmac_finish, scrypt_pbkdf2, scrypt_pbkdf2_1
- Types: scrypt_hmac_state_t

### scryptjane/scrypt-jane-portable-x86.h
- Functions: get_cpuid, get_xgetbv, _xgetbv, detect_cpu, get_top_cpuflag_desc
- Types: packedelem8_t, packedelem32_t, packedelem64_t, cpu_flags_x86_t, cpu_vendors_x86_t, x86_regs_t
- Macros: X86ASM, X86ASM_SSE, X86ASM_SSE2, X86ASM_SSSE3, X86ASM_AVX, X86_64ASM, X86_64ASM_SSE2, X86_64ASM_SSSE3, X86_64ASM_AVX, X86_INTRINSIC, X86_INTRINSIC_SSE, X86_INTRINSIC_SSE2, X86_INTRINSIC_SSSE3, X86_64USE_INTRINSIC, X86_INTRINSIC_AVX, a1, a2, a3, a4, al, aj, asm_align8, asm_align16, asm_calling_convention, asm_naked_fn_proto, asm_naked_fn, asm_naked_fn_end, GNU_AS1, GNU_AS2, GNU_AS3, GNU_AS4, GNU_ASL, GNU_ASFN, GNU_ASJ, aret, asm_gcc, asm_gcc_parms, asm_gcc_trashed, asm_gcc_end, cpuid_bx

### scryptjane/scrypt-jane-portable.h
- Functions: scrypt_verify, scrypt_ensure_zero, detect_cpu
- Macros:
  - `OS_WINDOWS`
  - `OS_SOLARIS`
  - `OS_NIX`
  - `OS_LINUX`
  - `OS_BSD`
  - `OS_OSX`
  - `OS_MAC`
  - `OS_OPENBSD`
  - `COMPILER_MSVC`
  - `COMPILER_MSVC6PP_AND_LATER`
  - `COMPILER_HAS_TMMINTRIN`
  - `ROTL32`
  - `ROTR32`
  - `ROTL64`
  - `ROTR64`
  - `NOINLINE`
  - `INLINE`
  - `FASTCALL`
  - `CDECL`
  - `STDCALL`
  - `NAKED`
  - `MM16`
  - `COMPILER_INTEL`
  - `COMPILER_GCC_PATCHLEVEL`
  - `COMPILER_GCC`
  - `COMPILER_MINGW`
  - `COMPILER_PATHCC`
  - `OPTIONAL_INLINE`
  - `CRYPTO_FN`
  - `CPU_X86_64`
  - `CPU_X86`
  - `CPU_IA64`
  - `CPU_SPARC`
  - `CPU_SPARC64`
  - `CPU_64BITS`
  - `CPU_PPC`
  - `CPU_POWER7`
  - `CPU_PPC64`
  - `CPU_PPC32`
  - `CPU_HPPA`
  - `CPU_ALPHA`
  - `CPU_LE`
  - `CPU_BE`
  - `U8TO32_BE`
  - `U8TO32_LE`
  - `U32TO8_BE`
  - `U32TO8_LE`
  - `U8TO64_BE`
  - `U8TO64_LE`
  - `U64TO8_BE`
  - `U64TO8_LE`
  - `U32_SWAP`
  - `U64_SWAP`

### scryptjane/scrypt-jane-romix-basic.h
- Functions: void, scrypt_test_mix_instance, scrypt_verify, scrypt_item, scrypt_block

### scryptjane/scrypt-jane-romix-template.h
- Functions: SCRYPT_ROMIX_FN, scrypt_ROMix_1
- Macros: SCRYPT_ROMIX_FN, SCRYPT_HAVE_ROMIX, SCRYPT_CHUNKMIX_FN

### scryptjane/scrypt-jane-romix.h
- Functions: scrypt_ROMix_error, scrypt_getROMix, scrypt_ROMix, scrypt_test_mix
- Macros: SCRYPT_MIX_BASE, SCRYPT_WORDTO8_LE, SCRYPT_WORD_ENDIAN_SWAP, SCRYPT_BLOCK_BYTES, SCRYPT_BLOCK_WORDS, SCRYPT_MIX

### scryptjane/scrypt-jane-salsa.h
- Functions: scrypt_getROMix, available_implementations, scrypt_test_mix
- Macros: SCRYPT_MIX_BASE, SCRYPT_WORDTO8_LE, SCRYPT_WORD_ENDIAN_SWAP, SCRYPT_BLOCK_BYTES, SCRYPT_BLOCK_WORDS, SCRYPT_CHUNKMIX_FN, SCRYPT_ROMIX_FN, SCRYPT_ROMIX_TANGLE_FN, SCRYPT_ROMIX_UNTANGLE_FN, SCRYPT_MIX_FN

### scryptjane/scrypt-jane-salsa64.h
- Functions: scrypt_getROMix, available_implementations, scrypt_test_mix
- Macros: SCRYPT_MIX_BASE, SCRYPT_WORDTO8_LE, SCRYPT_WORD_ENDIAN_SWAP, SCRYPT_BLOCK_BYTES, SCRYPT_BLOCK_WORDS, SCRYPT_CHUNKMIX_FN, SCRYPT_ROMIX_FN, SCRYPT_ROMIX_TANGLE_FN, SCRYPT_ROMIX_UNTANGLE_FN, SCRYPT_MIX_FN

### scryptjane/scrypt-jane-test-vectors.h
- Types: scrypt_test_setting_t

### sha3/aes_helper.c
- Macros: AESx, AES0, AES1, AES2, AES3, AES_ROUND_BE, AES_ROUND_NOKEY_BE, AES_ROUND_LE, AES_ROUND_NOKEY_LE

### sha3/gost_streebog.c
- Functions: AddModulo512, AddXor512, F, E, g_N, hash_X, hash_512, hash_256, sph_gost256_init, sph_gost256, sph_gost256_close, sph_gost256_addbits_and_close, sph_gost512_init, sph_gost512, sph_gost512_close, sph_gost512_addbits_and_close
- Macros: ADDBYTE_8, KeySchedule

### sha3/gost_streebog.h
- Functions: sph_gost256_init, sph_gost256, sph_gost256_close, sph_gost256_addbits_and_close, sph_gost512_init, sph_gost512, sph_gost512_close, sph_gost512_addbits_and_close
- Macros: SPH_GOST_H__, SPH_SIZE_gost256, SPH_SIZE_gost512

### sha3/haval_helper.c
- Functions: SPH_XCAT
- Macros: SPH_XCAT, SPH_XCAT_

### sha3/md_helper.c
- Functions: SPH_XCAT
- Macros: SPH_XCAT, SPH_XCAT_, SPH_BLEN, SPH_WLEN, SPH_MAXPAD, SPH_VAL, SPH_NO_OUTPUT

### sha3/mod_blakecoin.c
- Functions: blake32_init, blake32, blake32_close, blakecoin_init, blakecoin, blakecoin_addbits_and_close, blakecoin_close
- Macros:
  - `Z00`
  - `Z01`
  - `Z02`
  - `Z03`
  - `Z04`
  - `Z05`
  - `Z06`
  - `Z07`
  - `Z08`
  - `Z09`
  - `Z0A`
  - `Z0B`
  - `Z0C`
  - `Z0D`
  - `Z0E`
  - `Z0F`
  - `Z10`
  - `Z11`
  - `Z12`
  - `Z13`
  - `Z14`
  - `Z15`
  - `Z16`
  - `Z17`
  - `Z18`
  - `Z19`
  - `Z1A`
  - `Z1B`
  - `Z1C`
  - `Z1D`
  - `Z1E`
  - `Z1F`
  - `Z20`
  - `Z21`
  - `Z22`
  - `Z23`
  - `Z24`
  - `Z25`
  - `Z26`
  - `Z27`
  - `Z28`
  - `Z29`
  - `Z2A`
  - `Z2B`
  - `Z2C`
  - `Z2D`
  - `Z2E`
  - `Z2F`
  - `Z30`
  - `Z31`
  - `Z32`
  - `Z33`
  - `Z34`
  - `Z35`
  - `Z36`
  - `Z37`
  - `Z38`
  - `Z39`
  - `Z3A`
  - `Z3B`
  - `Z3C`
  - `Z3D`
  - `Z3E`
  - `Z3F`
  - `Z40`
  - `Z41`
  - `Z42`
  - `Z43`
  - `Z44`
  - `Z45`
  - `Z46`
  - `Z47`
  - `Z48`
  - `Z49`
  - `Z4A`
  - `Z4B`
  - `Z4C`
  - `Z4D`
  - `Z4E`
  - `Z4F`
  - `Z50`
  - `Z51`
  - `Z52`
  - `Z53`
  - `Z54`
  - `Z55`
  - `Z56`
  - `Z57`
  - `Z58`
  - `Z59`
  - `Z5A`
  - `Z5B`
  - `Z5C`
  - `Z5D`
  - `Z5E`
  - `Z5F`
  - `Z60`
  - `Z61`
  - `Z62`
  - `Z63`
  - `Z64`
  - `Z65`
  - `Z66`
  - `Z67`
  - `Z68`
  - `Z69`
  - `Z6A`
  - `Z6B`
  - `Z6C`
  - `Z6D`
  - `Z6E`
  - `Z6F`
  - `Z70`
  - `Z71`
  - `Z72`
  - `Z73`
  - `Z74`
  - `Z75`
  - `Z76`
  - `Z77`
  - `Z78`
  - `Z79`
  - `Z7A`
  - `Z7B`
  - `Z7C`
  - `Z7D`
  - `Z7E`
  - `Z7F`
  - `Z80`
  - `Z81`
  - `Z82`
  - `Z83`
  - `Z84`
  - `Z85`
  - `Z86`
  - `Z87`
  - `Z88`
  - `Z89`
  - `Z8A`
  - `Z8B`
  - `Z8C`
  - `Z8D`
  - `Z8E`
  - `Z8F`
  - `Z90`
  - `Z91`
  - `Z92`
  - `Z93`
  - `Z94`
  - `Z95`
  - `Z96`
  - `Z97`
  - `Z98`
  - `Z99`
  - `Z9A`
  - `Z9B`
  - `Z9C`
  - `Z9D`
  - `Z9E`
  - `Z9F`
  - `Mx`
  - `Mx_`
  - `Mx__`
  - `CSx`
  - `CSx_`
  - `CSx__`
  - `CS0`
  - `CS1`
  - `CS2`
  - `CS3`
  - `CS4`
  - `CS5`
  - `CS6`
  - `CS7`
  - `CS8`
  - `CS9`
  - `CSA`
  - `CSB`
  - `CSC`
  - `CSD`
  - `CSE`
  - `CSF`
  - `CBx`
  - `CBx_`
  - `CBx__`
  - `CB0`
  - `CB1`
  - `CB2`
  - `CB3`
  - `CB4`
  - `CB5`
  - `CB6`
  - `CB7`
  - `CB8`
  - `CB9`
  - `CBA`
  - `CBB`
  - `CBC`
  - `CBD`
  - `CBE`
  - `CBF`
  - `GS`
  - `ROUND_S`
  - `DECL_STATE32`
  - `READ_STATE32`
  - `WRITE_STATE32`
  - `BLAKE32_ROUNDS`
  - `COMPRESS32`

### sha3/sph_blake.c
- Functions: blake32_init, blake32, blake32_close, blake64_init, blake64, blake64_close, sph_blake224_init, sph_blake224, sph_blake224_close, sph_blake224_addbits_and_close, sph_blake256_init, sph_blake256, sph_blake256_close, sph_blake256_addbits_and_close, sph_blake384_init, sph_blake384, sph_blake384_close, sph_blake384_addbits_and_close, sph_blake512_init, sph_blake512, sph_blake512_close, sph_blake512_addbits_and_close
- Macros:
  - `SPH_SMALL_FOOTPRINT_BLAKE`
  - `SPH_COMPACT_BLAKE_32`
  - `SPH_COMPACT_BLAKE_64`
  - `Z00`
  - `Z01`
  - `Z02`
  - `Z03`
  - `Z04`
  - `Z05`
  - `Z06`
  - `Z07`
  - `Z08`
  - `Z09`
  - `Z0A`
  - `Z0B`
  - `Z0C`
  - `Z0D`
  - `Z0E`
  - `Z0F`
  - `Z10`
  - `Z11`
  - `Z12`
  - `Z13`
  - `Z14`
  - `Z15`
  - `Z16`
  - `Z17`
  - `Z18`
  - `Z19`
  - `Z1A`
  - `Z1B`
  - `Z1C`
  - `Z1D`
  - `Z1E`
  - `Z1F`
  - `Z20`
  - `Z21`
  - `Z22`
  - `Z23`
  - `Z24`
  - `Z25`
  - `Z26`
  - `Z27`
  - `Z28`
  - `Z29`
  - `Z2A`
  - `Z2B`
  - `Z2C`
  - `Z2D`
  - `Z2E`
  - `Z2F`
  - `Z30`
  - `Z31`
  - `Z32`
  - `Z33`
  - `Z34`
  - `Z35`
  - `Z36`
  - `Z37`
  - `Z38`
  - `Z39`
  - `Z3A`
  - `Z3B`
  - `Z3C`
  - `Z3D`
  - `Z3E`
  - `Z3F`
  - `Z40`
  - `Z41`
  - `Z42`
  - `Z43`
  - `Z44`
  - `Z45`
  - `Z46`
  - `Z47`
  - `Z48`
  - `Z49`
  - `Z4A`
  - `Z4B`
  - `Z4C`
  - `Z4D`
  - `Z4E`
  - `Z4F`
  - `Z50`
  - `Z51`
  - `Z52`
  - `Z53`
  - `Z54`
  - `Z55`
  - `Z56`
  - `Z57`
  - `Z58`
  - `Z59`
  - `Z5A`
  - `Z5B`
  - `Z5C`
  - `Z5D`
  - `Z5E`
  - `Z5F`
  - `Z60`
  - `Z61`
  - `Z62`
  - `Z63`
  - `Z64`
  - `Z65`
  - `Z66`
  - `Z67`
  - `Z68`
  - `Z69`
  - `Z6A`
  - `Z6B`
  - `Z6C`
  - `Z6D`
  - `Z6E`
  - `Z6F`
  - `Z70`
  - `Z71`
  - `Z72`
  - `Z73`
  - `Z74`
  - `Z75`
  - `Z76`
  - `Z77`
  - `Z78`
  - `Z79`
  - `Z7A`
  - `Z7B`
  - `Z7C`
  - `Z7D`
  - `Z7E`
  - `Z7F`
  - `Z80`
  - `Z81`
  - `Z82`
  - `Z83`
  - `Z84`
  - `Z85`
  - `Z86`
  - `Z87`
  - `Z88`
  - `Z89`
  - `Z8A`
  - `Z8B`
  - `Z8C`
  - `Z8D`
  - `Z8E`
  - `Z8F`
  - `Z90`
  - `Z91`
  - `Z92`
  - `Z93`
  - `Z94`
  - `Z95`
  - `Z96`
  - `Z97`
  - `Z98`
  - `Z99`
  - `Z9A`
  - `Z9B`
  - `Z9C`
  - `Z9D`
  - `Z9E`
  - `Z9F`
  - `Mx`
  - `Mx_`
  - `Mx__`
  - `CSx`
  - `CSx_`
  - `CSx__`
  - `CS0`
  - `CS1`
  - `CS2`
  - `CS3`
  - `CS4`
  - `CS5`
  - `CS6`
  - `CS7`
  - `CS8`
  - `CS9`
  - `CSA`
  - `CSB`
  - `CSC`
  - `CSD`
  - `CSE`
  - `CSF`
  - `CBx`
  - `CBx_`
  - `CBx__`
  - `CB0`
  - `CB1`
  - `CB2`
  - `CB3`
  - `CB4`
  - `CB5`
  - `CB6`
  - `CB7`
  - `CB8`
  - `CB9`
  - `CBA`
  - `CBB`
  - `CBC`
  - `CBD`
  - `CBE`
  - `CBF`
  - `GS`
  - `ROUND_S`
  - `GB`
  - `ROUND_B`
  - `DECL_STATE32`
  - `READ_STATE32`
  - `WRITE_STATE32`
  - `BLAKE32_ROUNDS`
  - `COMPRESS32`
  - `DECL_STATE64`
  - `READ_STATE64`
  - `WRITE_STATE64`
  - `COMPRESS64`

### sha3/sph_blake.h
- Functions: sph_blake224_init, sph_blake224, sph_blake224_close, sph_blake224_addbits_and_close, sph_blake256_init, sph_blake256, sph_blake256_close, sph_blake256_addbits_and_close, sph_blake384_init, sph_blake384, sph_blake384_close, sph_blake384_addbits_and_close, sph_blake512_init, sph_blake512, sph_blake512_close, sph_blake512_addbits_and_close
- Macros: SPH_BLAKE_H__, SPH_SIZE_blake224, SPH_SIZE_blake256, SPH_SIZE_blake384, SPH_SIZE_blake512

### sha3/sph_bmw.c
- Functions: compress_small, bmw32_init, bmw32, bmw32_close, compress_big, bmw64_init, bmw64, bmw64_close, sph_bmw224_init, sph_bmw224, sph_bmw224_close, sph_bmw224_addbits_and_close, sph_bmw256_init, sph_bmw256, sph_bmw256_close, sph_bmw256_addbits_and_close, sph_bmw384_init, sph_bmw384, sph_bmw384_close, sph_bmw384_addbits_and_close, sph_bmw512_init, sph_bmw512, sph_bmw512_close, sph_bmw512_addbits_and_close
- Macros:
  - `SPH_SMALL_FOOTPRINT_BMW`
  - `XCAT`
  - `XCAT_`
  - `LPAR`
  - `I16_16`
  - `I16_17`
  - `I16_18`
  - `I16_19`
  - `I16_20`
  - `I16_21`
  - `I16_22`
  - `I16_23`
  - `I16_24`
  - `I16_25`
  - `I16_26`
  - `I16_27`
  - `I16_28`
  - `I16_29`
  - `I16_30`
  - `I16_31`
  - `M16_16`
  - `M16_17`
  - `M16_18`
  - `M16_19`
  - `M16_20`
  - `M16_21`
  - `M16_22`
  - `M16_23`
  - `M16_24`
  - `M16_25`
  - `M16_26`
  - `M16_27`
  - `M16_28`
  - `M16_29`
  - `M16_30`
  - `M16_31`
  - `ss0`
  - `ss1`
  - `ss2`
  - `ss3`
  - `ss4`
  - `ss5`
  - `rs1`
  - `rs2`
  - `rs3`
  - `rs4`
  - `rs5`
  - `rs6`
  - `rs7`
  - `Ks`
  - `add_elt_s`
  - `expand1s_inner`
  - `expand1s`
  - `expand1s_`
  - `expand2s_inner`
  - `expand2s`
  - `expand2s_`
  - `sb0`
  - `sb1`
  - `sb2`
  - `sb3`
  - `sb4`
  - `sb5`
  - `rb1`
  - `rb2`
  - `rb3`
  - `rb4`
  - `rb5`
  - `rb6`
  - `rb7`
  - `Kb`
  - `rol_off`
  - `add_elt_b`
  - `expand1b`
  - `expand2b`
  - `expand1b_inner`
  - `expand1b_`
  - `expand2b_inner`
  - `expand2b_`
  - `MAKE_W`
  - `Ws0`
  - `Ws1`
  - `Ws2`
  - `Ws3`
  - `Ws4`
  - `Ws5`
  - `Ws6`
  - `Ws7`
  - `Ws8`
  - `Ws9`
  - `Ws10`
  - `Ws11`
  - `Ws12`
  - `Ws13`
  - `Ws14`
  - `Ws15`
  - `MAKE_Qas`
  - `MAKE_Qbs`
  - `MAKE_Qs`
  - `Qs`
  - `Wb0`
  - `Wb1`
  - `Wb2`
  - `Wb3`
  - `Wb4`
  - `Wb5`
  - `Wb6`
  - `Wb7`
  - `Wb8`
  - `Wb9`
  - `Wb10`
  - `Wb11`
  - `Wb12`
  - `Wb13`
  - `Wb14`
  - `Wb15`
  - `MAKE_Qab`
  - `MAKE_Qbb`
  - `MAKE_Qb`
  - `Qb`
  - `FOLD`
  - `FOLDs`
  - `FOLDb`
  - `M`
  - `H`
  - `dH`

### sha3/sph_bmw.h
- Functions: sph_bmw224_init, sph_bmw224, sph_bmw224_close, sph_bmw224_addbits_and_close, sph_bmw256_init, sph_bmw256, sph_bmw256_close, sph_bmw256_addbits_and_close, sph_bmw384_init, sph_bmw384, sph_bmw384_close, sph_bmw384_addbits_and_close, sph_bmw512_init, sph_bmw512, sph_bmw512_close, sph_bmw512_addbits_and_close
- Macros: SPH_BMW_H__, SPH_SIZE_bmw224, SPH_SIZE_bmw256, SPH_SIZE_bmw384, SPH_SIZE_bmw512

### sha3/sph_cubehash.c
- Functions: cubehash_init, cubehash_core, cubehash_close, sph_cubehash224_init, sph_cubehash224, sph_cubehash224_close, sph_cubehash224_addbits_and_close, sph_cubehash256_init, sph_cubehash256, sph_cubehash256_close, sph_cubehash256_addbits_and_close, sph_cubehash384_init, sph_cubehash384, sph_cubehash384_close, sph_cubehash384_addbits_and_close, sph_cubehash512_init, sph_cubehash512, sph_cubehash512_close, sph_cubehash512_addbits_and_close
- Macros: SPH_SMALL_FOOTPRINT_CUBEHASH, SPH_CUBEHASH_UNROLL, SPH_CUBEHASH_NOCOPY, T32, ROTL32, DECL_STATE, READ_STATE, WRITE_STATE, x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, xa, xb, xc, xd, xe, xf, xg, xh, xi, xj, xk, xl, xm, xn, xo, xp, xq, xr, xs, xt, xu, xv, INPUT_BLOCK, ROUND_EVEN, ROUND_ODD, SIXTEEN_ROUNDS

### sha3/sph_cubehash.h
- Functions: sph_cubehash224_init, sph_cubehash224, sph_cubehash224_close, sph_cubehash224_addbits_and_close, sph_cubehash256_init, sph_cubehash256, sph_cubehash256_close, sph_cubehash256_addbits_and_close, sph_cubehash384_init, sph_cubehash384, sph_cubehash384_close, sph_cubehash384_addbits_and_close, sph_cubehash512_init, sph_cubehash512, sph_cubehash512_close, sph_cubehash512_addbits_and_close
- Macros: SPH_CUBEHASH_H__, SPH_SIZE_cubehash224, SPH_SIZE_cubehash256, SPH_SIZE_cubehash384, SPH_SIZE_cubehash512

### sha3/sph_echo.c
- Functions: aes_2rounds_all, mix_column, echo_small_init, echo_big_init, echo_small_compress, COMPRESS_SMALL, echo_big_compress, COMPRESS_BIG, echo_small_core, echo_big_core, echo_small_close, echo_big_close, sph_echo224_init, sph_echo224, sph_echo224_close, sph_echo224_addbits_and_close, sph_echo256_init, sph_echo256, sph_echo256_close, sph_echo256_addbits_and_close, sph_echo384_init, sph_echo384, sph_echo384_close, sph_echo384_addbits_and_close, sph_echo512_init, sph_echo512, sph_echo512_close, sph_echo512_addbits_and_close
- Macros: SPH_SMALL_FOOTPRINT_ECHO, SPH_ECHO_64, T32, C32, C64, AES_BIG_ENDIAN, DECL_STATE_SMALL, DECL_STATE_BIG, INPUT_BLOCK_SMALL, INPUT_BLOCK_BIG, BIG_SUB_WORDS, AES_2ROUNDS, SHIFT_ROW1, SHIFT_ROW2, SHIFT_ROW3, BIG_SHIFT_ROWS, MIX_COLUMN, MIX_COLUMN1, BIG_MIX_COLUMNS, BIG_ROUND, FINAL_SMALL, FINAL_BIG, COMPRESS_SMALL, COMPRESS_BIG, INCR_COUNTER

### sha3/sph_echo.h
- Functions: sph_echo224_init, sph_echo224, sph_echo224_close, sph_echo224_addbits_and_close, sph_echo256_init, sph_echo256, sph_echo256_close, sph_echo256_addbits_and_close, sph_echo384_init, sph_echo384, sph_echo384_close, sph_echo384_addbits_and_close, sph_echo512_init, sph_echo512, sph_echo512_close, sph_echo512_addbits_and_close
- Macros: SPH_ECHO_H__, SPH_SIZE_echo224, SPH_SIZE_echo256, SPH_SIZE_echo384, SPH_SIZE_echo512

### sha3/sph_fugue.c
- Functions: fugue_init, fugue2_core, READ_STATE_SMALL, WRITE_STATE_SMALL, fugue3_core, READ_STATE_BIG, WRITE_STATE_BIG, fugue4_core, fugue2_close, fugue3_close, fugue4_close, sph_fugue224_init, sph_fugue224, sph_fugue224_close, sph_fugue224_addbits_and_close, sph_fugue256_init, sph_fugue256, sph_fugue256_close, sph_fugue256_addbits_and_close, sph_fugue384_init, sph_fugue384, sph_fugue384_close, sph_fugue384_addbits_and_close, sph_fugue512_init, sph_fugue512, sph_fugue512_close, sph_fugue512_addbits_and_close
- Macros: TIX2, TIX3, TIX4, CMIX30, CMIX36, SMIX, DECL_STATE_SMALL, READ_STATE_SMALL, WRITE_STATE_SMALL, DECL_STATE_BIG, READ_STATE_BIG, WRITE_STATE_BIG, S00, S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S35, INCR_COUNTER, CORE_ENTRY, CORE_EXIT, NEXT, WRITE_COUNTER, CLOSE_ENTRY, ROR

### sha3/sph_fugue.h
- Functions: sph_fugue224_init, sph_fugue224, sph_fugue224_close, sph_fugue224_addbits_and_close, sph_fugue256_init, sph_fugue256, sph_fugue256_close, sph_fugue256_addbits_and_close, sph_fugue384_init, sph_fugue384, sph_fugue384_close, sph_fugue384_addbits_and_close, sph_fugue512_init, sph_fugue512, sph_fugue512_close, sph_fugue512_addbits_and_close
- Macros: SPH_FUGUE_H__, SPH_SIZE_fugue224, SPH_SIZE_fugue256, SPH_SIZE_fugue384, SPH_SIZE_fugue512

### sha3/sph_groestl.c
- Functions: groestl_small_init, groestl_small_core, groestl_small_close, groestl_big_init, groestl_big_core, groestl_big_close, sph_groestl224_init, sph_groestl224, sph_groestl224_close, sph_groestl224_addbits_and_close, sph_groestl256_init, sph_groestl256, sph_groestl256_close, sph_groestl256_addbits_and_close, sph_groestl384_init, sph_groestl384, sph_groestl384_close, sph_groestl384_addbits_and_close, sph_groestl512_init, sph_groestl512, sph_groestl512_close, sph_groestl512_addbits_and_close
- Macros: SPH_SMALL_FOOTPRINT_GROESTL, SPH_GROESTL_64, USE_LE, C32e, dec32e_aligned, enc32e, B32_0, B32_1, B32_2, B32_3, R32u, R32d, PC32up, PC32dn, QC32up, QC32dn, C64e, dec64e_aligned, enc64e, B64_0, B64_1, B64_2, B64_3, B64_4, B64_5, B64_6, B64_7, R64, PC64, QC64, DECL_STATE_SMALL, READ_STATE_SMALL, WRITE_STATE_SMALL, RSTT, ROUND_SMALL_P, ROUND_SMALL_Q, PERM_SMALL_P, PERM_SMALL_Q, COMPRESS_SMALL, FINAL_SMALL, DECL_STATE_BIG, READ_STATE_BIG, WRITE_STATE_BIG, RBTT, ROUND_BIG_P, ROUND_BIG_Q, PERM_BIG_P, PERM_BIG_Q, COMPRESS_BIG, FINAL_BIG, XCAT, XCAT_

### sha3/sph_groestl.h
- Functions: sph_groestl224_init, sph_groestl224, sph_groestl224_close, sph_groestl224_addbits_and_close, sph_groestl256_init, sph_groestl256, sph_groestl256_close, sph_groestl256_addbits_and_close, sph_groestl384_init, sph_groestl384, sph_groestl384_close, sph_groestl384_addbits_and_close, sph_groestl512_init, sph_groestl512, sph_groestl512_close, sph_groestl512_addbits_and_close
- Macros: SPH_GROESTL_H__, SPH_SIZE_groestl224, SPH_SIZE_groestl256, SPH_SIZE_groestl384, SPH_SIZE_groestl512

### sha3/sph_hamsi.c
- Functions: hamsi_small, hamsi_small_final, READ_STATE_SMALL, hamsi_small_init, hamsi_small_core, hamsi_small_close, hamsi_big, hamsi_big_final, READ_STATE_BIG, hamsi_big_init, hamsi_big_core, hamsi_big_close, sph_hamsi224_init, sph_hamsi224, sph_hamsi224_close, sph_hamsi224_addbits_and_close, sph_hamsi256_init, sph_hamsi256, sph_hamsi256_close, sph_hamsi256_addbits_and_close, sph_hamsi384_init, sph_hamsi384, sph_hamsi384_close, sph_hamsi384_addbits_and_close, sph_hamsi512_init, sph_hamsi512, sph_hamsi512_close, sph_hamsi512_addbits_and_close
- Macros: SPH_SMALL_FOOTPRINT_HAMSI, SPH_HAMSI_EXPAND_SMALL, SPH_HAMSI_EXPAND_BIG, DECL_STATE_SMALL, READ_STATE_SMALL, WRITE_STATE_SMALL, s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, sA, sB, sC, sD, sE, sF, SBOX, L, ROUND_SMALL, P_SMALL, PF_SMALL, T_SMALL, DECL_STATE_BIG, READ_STATE_BIG, WRITE_STATE_BIG, s00, s01, s02, s03, s04, s05, s06, s07, s08, s09, s0A, s0B, s0C, s0D, s0E, s0F, s10, s11, s12, s13, s14, s15, s16, s17, s18, s19, s1A, s1B, s1C, s1D, s1E, s1F, ROUND_BIG, P_BIG, PF_BIG, T_BIG

### sha3/sph_hamsi.h
- Functions: sph_hamsi224_init, sph_hamsi224, sph_hamsi224_close, sph_hamsi224_addbits_and_close, sph_hamsi256_init, sph_hamsi256, sph_hamsi256_close, sph_hamsi256_addbits_and_close, sph_hamsi384_init, sph_hamsi384, sph_hamsi384_close, sph_hamsi384_addbits_and_close, sph_hamsi512_init, sph_hamsi512, sph_hamsi512_close, sph_hamsi512_addbits_and_close
- Macros: SPH_HAMSI_H__, SPH_SIZE_hamsi224, SPH_SIZE_hamsi256, SPH_SIZE_hamsi384, SPH_SIZE_hamsi512

### sha3/sph_hamsi_helper.c
- Macros: INPUT_SMALL, INPUT_BIG

### sha3/sph_haval.c
- Functions: haval_init, mix128, mix160_0, SPH_ROTL32, mix160_1, mix160_2, mix160_3, mix160_4, mix192_0, mix192_1, mix192_2, mix192_3, mix192_4, mix192_5, haval_out, sph_haval_3_comp, sph_haval_4_comp, sph_haval_5_comp
- Macros: SPH_SMALL_FOOTPRINT_HAVAL, F1, F2, F3, F4, F5, FP3_1, FP3_2, FP3_3, FP4_1, FP4_2, FP4_3, FP4_4, FP5_1, FP5_2, FP5_3, FP5_4, FP5_5, STEP, PASS1, PASSG, PASS2, PASS3, PASS4, PASS5, SAVE_STATE, UPDATE_STATE, CORE3, CORE4, CORE5, DSTATE, RSTATE, WSTATE, IN_PREPARE, INW, PASSES, API, RVAL, WVAL, INMSG

### sha3/sph_haval.h
- Functions:
  - `sph_haval128_3_init`
  - `sph_haval128_3`
  - `sph_haval128_3_close`
  - `sph_haval128_3_addbits_and_close`
  - `sph_haval128_4_init`
  - `sph_haval128_4`
  - `sph_haval128_4_close`
  - `sph_haval128_4_addbits_and_close`
  - `sph_haval128_5_init`
  - `sph_haval128_5`
  - `sph_haval128_5_close`
  - `sph_haval128_5_addbits_and_close`
  - `sph_haval160_3_init`
  - `sph_haval160_3`
  - `sph_haval160_3_close`
  - `sph_haval160_3_addbits_and_close`
  - `sph_haval160_4_init`
  - `sph_haval160_4`
  - `sph_haval160_4_close`
  - `sph_haval160_5_init`
  - `sph_haval160_5`
  - `sph_haval160_5_close`
  - `sph_haval160_5_addbits_and_close`
  - `sph_haval192_3_init`
  - `sph_haval192_3`
  - `sph_haval192_3_close`
  - `sph_haval192_3_addbits_and_close`
  - `sph_haval192_4_init`
  - `sph_haval192_4`
  - `sph_haval192_4_close`
  - `sph_haval192_4_addbits_and_close`
  - `sph_haval192_5_init`
  - `sph_haval192_5`
  - `sph_haval192_5_close`
  - `sph_haval192_5_addbits_and_close`
  - `sph_haval224_3_init`
  - `sph_haval224_3`
  - `sph_haval224_3_close`
  - `sph_haval224_3_addbits_and_close`
  - `sph_haval224_4_init`
  - `sph_haval224_4`
  - `sph_haval224_4_close`
  - `sph_haval224_4_addbits_and_close`
  - `sph_haval224_5_init`
  - `sph_haval224_5`
  - `sph_haval224_5_close`
  - `sph_haval224_5_addbits_and_close`
  - `sph_haval256_3_init`
  - `sph_haval256_3`
  - `sph_haval256_3_close`
  - `sph_haval256_3_addbits_and_close`
  - `sph_haval256_4_init`
  - `sph_haval256_4`
  - `sph_haval256_4_close`
  - `sph_haval256_4_addbits_and_close`
  - `sph_haval256_5_init`
  - `sph_haval256_5`
  - `sph_haval256_5_close`
  - `sph_haval256_5_addbits_and_close`
  - `sph_haval_3_comp`
  - `sph_haval_4_comp`
  - `sph_haval_5_comp`
- Macros: SPH_HAVAL_H__, SPH_SIZE_haval128_3, SPH_SIZE_haval128_4, SPH_SIZE_haval128_5, SPH_SIZE_haval160_3, SPH_SIZE_haval160_4, SPH_SIZE_haval160_5, SPH_SIZE_haval192_3, SPH_SIZE_haval192_4, SPH_SIZE_haval192_5, SPH_SIZE_haval224_3, SPH_SIZE_haval224_4, SPH_SIZE_haval224_5, SPH_SIZE_haval256_3, SPH_SIZE_haval256_4, SPH_SIZE_haval256_5

### sha3/sph_hefty1.c
- Functions: Rr, Ch, Sigma1, sigma1, Ma, Sigma0, sigma0, Reverse32, Reverse64, Smoosh4, Smoosh2, Mangle, Absorb, Squeeze, Br, HashBlock, HEFTY1_Init, HEFTY1_Update, HEFTY1_Final, HEFTY1
- Macros: inline, Min, RoundFunc

### sha3/sph_hefty1.h
- Functions: HEFTY1_Init, HEFTY1_Update, HEFTY1_Final, HEFTY1
- Types: HEFTY1_CTX
- Macros: __HEFTY1_H__, HEFTY1_DIGEST_BYTES, HEFTY1_BLOCK_BYTES, HEFTY1_STATE_WORDS, HEFTY1_SPONGE_WORDS

### sha3/sph_jh.c
- Functions: jh_init, jh_core, jh_close, sph_jh224_init, sph_jh224, sph_jh224_close, sph_jh224_addbits_and_close, sph_jh256_init, sph_jh256, sph_jh256_close, sph_jh256_addbits_and_close, sph_jh384_init, sph_jh384, sph_jh384_close, sph_jh384_addbits_and_close, sph_jh512_init, sph_jh512, sph_jh512_close, sph_jh512_addbits_and_close
- Macros: SPH_SMALL_FOOTPRINT_JH, SPH_JH_64, C32e, dec32e_aligned, enc32e, C64e, dec64e_aligned, enc64e, Sb, Lb, Ceven_hi, Ceven_lo, Codd_hi, Codd_lo, S, L, Wz, W0, W1, W2, W3, W4, W5, W6, DECL_STATE, READ_STATE, WRITE_STATE, INPUT_BUF1, INPUT_BUF2, Ceven_w3, Ceven_w2, Ceven_w1, Ceven_w0, Codd_w3, Codd_w2, Codd_w1, Codd_w0, SL, SLu, E8

### sha3/sph_jh.h
- Functions: sph_jh224_init, sph_jh224, sph_jh224_close, sph_jh224_addbits_and_close, sph_jh256_init, sph_jh256, sph_jh256_close, sph_jh256_addbits_and_close, sph_jh384_init, sph_jh384, sph_jh384_close, sph_jh384_addbits_and_close, sph_jh512_init, sph_jh512, sph_jh512_close, sph_jh512_addbits_and_close
- Macros: SPH_JH_H__, SPH_SIZE_jh224, SPH_SIZE_jh256, SPH_SIZE_jh384, SPH_SIZE_jh512

### sha3/sph_keccak.c
- Functions: keccak_init, keccak_core, sph_keccak224_init, sph_keccak224, sph_keccak224_close, sph_keccak224_addbits_and_close, sph_keccak256_init, sph_keccak256, sph_keccak256_close, sph_keccak256_addbits_and_close, sph_keccak384_init, sph_keccak384, sph_keccak384_close, sph_keccak384_addbits_and_close, sph_keccak512_init, sph_keccak512, sph_keccak512_close, sph_keccak512_addbits_and_close
- Macros:
  - `SPH_SMALL_FOOTPRINT_KECCAK`
  - `SPH_KECCAK_64`
  - `SPH_KECCAK_INTERLEAVE`
  - `SPH_KECCAK_UNROLL`
  - `SPH_KECCAK_NOCOPY`
  - `a00`
  - `a10`
  - `a20`
  - `a30`
  - `a40`
  - `a01`
  - `a11`
  - `a21`
  - `a31`
  - `a41`
  - `a02`
  - `a12`
  - `a22`
  - `a32`
  - `a42`
  - `a03`
  - `a13`
  - `a23`
  - `a33`
  - `a43`
  - `a04`
  - `a14`
  - `a24`
  - `a34`
  - `a44`
  - `DECL_STATE`
  - `READ_STATE`
  - `WRITE_STATE`
  - `INPUT_BUF`
  - `INPUT_BUF144`
  - `INPUT_BUF136`
  - `INPUT_BUF104`
  - `INPUT_BUF72`
  - `DECL64`
  - `MOV64`
  - `XOR64`
  - `AND64`
  - `OR64`
  - `NOT64`
  - `ROL64`
  - `XOR64_IOTA`
  - `INTERLEAVE`
  - `UNINTERLEAVE`
  - `a00l`
  - `a00h`
  - `a10l`
  - `a10h`
  - `a20l`
  - `a20h`
  - `a30l`
  - `a30h`
  - `a40l`
  - `a40h`
  - `a01l`
  - `a01h`
  - `a11l`
  - `a11h`
  - `a21l`
  - `a21h`
  - `a31l`
  - `a31h`
  - `a41l`
  - `a41h`
  - `a02l`
  - `a02h`
  - `a12l`
  - `a12h`
  - `a22l`
  - `a22h`
  - `a32l`
  - `a32h`
  - `a42l`
  - `a42h`
  - `a03l`
  - `a03h`
  - `a13l`
  - `a13h`
  - `a23l`
  - `a23h`
  - `a33l`
  - `a33h`
  - `a43l`
  - `a43h`
  - `a04l`
  - `a04h`
  - `a14l`
  - `a14h`
  - `a24l`
  - `a24h`
  - `a34l`
  - `a34h`
  - `a44l`
  - `a44h`
  - `READ64`
  - `ROL64_odd1`
  - `ROL64_odd63`
  - `ROL64_odd`
  - `ROL64_even`
  - `ROL64_0`
  - `ROL64_1`
  - `ROL64_2`
  - `ROL64_3`
  - `ROL64_4`
  - `ROL64_5`
  - `ROL64_6`
  - `ROL64_7`
  - `ROL64_8`
  - `ROL64_9`
  - `ROL64_10`
  - `ROL64_11`
  - `ROL64_12`
  - `ROL64_13`
  - `ROL64_14`
  - `ROL64_15`
  - `ROL64_16`
  - `ROL64_17`
  - `ROL64_18`
  - `ROL64_19`
  - `ROL64_20`
  - `ROL64_21`
  - `ROL64_22`
  - `ROL64_23`
  - `ROL64_24`
  - `ROL64_25`
  - `ROL64_26`
  - `ROL64_27`
  - `ROL64_28`
  - `ROL64_29`
  - `ROL64_30`
  - `ROL64_31`
  - `ROL64_32`
  - `ROL64_33`
  - `ROL64_34`
  - `ROL64_35`
  - `ROL64_36`
  - `ROL64_37`
  - `ROL64_38`
  - `ROL64_39`
  - `ROL64_40`
  - `ROL64_41`
  - `ROL64_42`
  - `ROL64_43`
  - `ROL64_44`
  - `ROL64_45`
  - `ROL64_46`
  - `ROL64_47`
  - `ROL64_48`
  - `ROL64_49`
  - `ROL64_50`
  - `ROL64_51`
  - `ROL64_52`
  - `ROL64_53`
  - `ROL64_54`
  - `ROL64_55`
  - `ROL64_56`
  - `ROL64_57`
  - `ROL64_58`
  - `ROL64_59`
  - `ROL64_60`
  - `ROL64_61`
  - `ROL64_62`
  - `ROL64_63`
  - `ROL64_small`
  - `ROL64_big`
  - `TH_ELT`
  - `THETA`
  - `RHO`
  - `KHI_XO`
  - `KHI_XA`
  - `KHI`
  - `IOTA`
  - `P0`
  - `P1`
  - `P2`
  - `P3`
  - `P4`
  - `P5`
  - `P6`
  - `P7`
  - `P8`
  - `P9`
  - `P10`
  - `P11`
  - `P12`
  - `P13`
  - `P14`
  - `P15`
  - `P16`
  - `P17`
  - `P18`
  - `P19`
  - `P20`
  - `P21`
  - `P22`
  - `P23`
  - `P1_TO_P0`
  - `P2_TO_P0`
  - `P4_TO_P0`
  - `P6_TO_P0`
  - `P8_TO_P0`
  - `P12_TO_P0`
  - `LPAR`
  - `RPAR`
  - `KF_ELT`
  - `DO`
  - `KECCAK_F_1600`
  - `KECCAK_F_1600_`
  - `DEFCLOSE`

### sha3/sph_keccak.h
- Functions: sph_keccak224_init, sph_keccak224, sph_keccak224_close, sph_keccak224_addbits_and_close, sph_keccak256_init, sph_keccak256, sph_keccak256_close, sph_keccak256_addbits_and_close, sph_keccak384_init, sph_keccak384, sph_keccak384_close, sph_keccak384_addbits_and_close, sph_keccak512_init, sph_keccak512, sph_keccak512_close, sph_keccak512_addbits_and_close
- Macros: SPH_KECCAK_H__, SPH_SIZE_keccak224, SPH_SIZE_keccak256, SPH_SIZE_keccak384, SPH_SIZE_keccak512

### sha3/sph_luffa.c
- Functions: luffa3, luffa3_close, luffa4, luffa4_close, luffa5, luffa5_close, sph_luffa224_init, sph_luffa224, sph_luffa224_close, sph_luffa224_addbits_and_close, sph_luffa256_init, sph_luffa256, sph_luffa256_close, sph_luffa256_addbits_and_close, sph_luffa384_init, sph_luffa384, sph_luffa384_close, sph_luffa384_addbits_and_close, sph_luffa512_init, sph_luffa512, sph_luffa512_close, sph_luffa512_addbits_and_close
- Macros: SPH_LUFFA_PARALLEL, DECL_TMP8, M2, XOR, SUB_CRUMB_GEN, SUB_CRUMB, SUB_CRUMBW, ROL32W, MIX_WORDW, MIX_WORD, DECL_STATE3, READ_STATE3, WRITE_STATE3, MI3, TWEAK3, P3, DECL_STATE4, READ_STATE4, WRITE_STATE4, MI4, TWEAK4, P4, DECL_STATE5, READ_STATE5, WRITE_STATE5, MI5, TWEAK5, P5

### sha3/sph_luffa.h
- Functions: sph_luffa224_init, sph_luffa224, sph_luffa224_close, sph_luffa224_addbits_and_close, sph_luffa256_init, sph_luffa256, sph_luffa256_close, sph_luffa256_addbits_and_close, sph_luffa384_init, sph_luffa384, sph_luffa384_close, sph_luffa384_addbits_and_close, sph_luffa512_init, sph_luffa512, sph_luffa512_close, sph_luffa512_addbits_and_close
- Macros: SPH_LUFFA_H__, SPH_SIZE_luffa224, SPH_SIZE_luffa256, SPH_SIZE_luffa384, SPH_SIZE_luffa512

### sha3/sph_panama.c
- Functions: panama_push, panama_pull, sph_panama_init, sph_panama, sph_panama_close
- Macros: LVAR17, LVARS, M17, BUPDATE1, BUPDATE, RSTATE, WSTATE, GAMMA, PI_ALL, THETA, SIGMA_ALL, PANAMA_STEP, INC0, INC1, INC2, INC3, INC4, INC5, INC6, INC7, INW1, INW2, INW_H1, INW_H2

### sha3/sph_panama.h
- Functions: sph_panama_init, sph_panama, sph_panama_close
- Macros: SPH_PANAMA_H__, SPH_SIZE_panama

### sha3/sph_radiogatun.c
- Functions: DECL19, DECL13, radiogatun32_push13, sph_radiogatun32_init, sph_radiogatun32, sph_radiogatun32_close, radiogatun64_push13, sph_radiogatun64_init, sph_radiogatun64, sph_radiogatun64_close
- Macros:
  - `SPH_SMALL_FOOTPRINT_RADIOGATUN`
  - `MUL19`
  - `DECL19`
  - `M19_T7`
  - `M19_T7_`
  - `M19_T7_0`
  - `M19_T7_1`
  - `M19_T7_2`
  - `M19_T7_3`
  - `M19_T7_4`
  - `M19_T7_5`
  - `M19_T7_6`
  - `M19_T7_7`
  - `M19_T7_8`
  - `M19_T7_9`
  - `M19_T7_10`
  - `M19_T7_11`
  - `M19_T7_12`
  - `M19_T7_13`
  - `M19_T7_14`
  - `M19_T7_15`
  - `M19_T7_16`
  - `M19_T7_17`
  - `M19_T7_18`
  - `M19_A1`
  - `M19_A1_`
  - `M19_A1_0`
  - `M19_A1_1`
  - `M19_A1_2`
  - `M19_A1_3`
  - `M19_A1_4`
  - `M19_A1_5`
  - `M19_A1_6`
  - `M19_A1_7`
  - `M19_A1_8`
  - `M19_A1_9`
  - `M19_A1_10`
  - `M19_A1_11`
  - `M19_A1_12`
  - `M19_A1_13`
  - `M19_A1_14`
  - `M19_A1_15`
  - `M19_A1_16`
  - `M19_A1_17`
  - `M19_A1_18`
  - `M19_A2`
  - `M19_A2_`
  - `M19_A2_0`
  - `M19_A2_1`
  - `M19_A2_2`
  - `M19_A2_3`
  - `M19_A2_4`
  - `M19_A2_5`
  - `M19_A2_6`
  - `M19_A2_7`
  - `M19_A2_8`
  - `M19_A2_9`
  - `M19_A2_10`
  - `M19_A2_11`
  - `M19_A2_12`
  - `M19_A2_13`
  - `M19_A2_14`
  - `M19_A2_15`
  - `M19_A2_16`
  - `M19_A2_17`
  - `M19_A2_18`
  - `M19_A4`
  - `M19_A4_`
  - `M19_A4_0`
  - `M19_A4_1`
  - `M19_A4_2`
  - `M19_A4_3`
  - `M19_A4_4`
  - `M19_A4_5`
  - `M19_A4_6`
  - `M19_A4_7`
  - `M19_A4_8`
  - `M19_A4_9`
  - `M19_A4_10`
  - `M19_A4_11`
  - `M19_A4_12`
  - `M19_A4_13`
  - `M19_A4_14`
  - `M19_A4_15`
  - `M19_A4_16`
  - `M19_A4_17`
  - `M19_A4_18`
  - `ACC_a`
  - `ACC_a_`
  - `ACC_atmp`
  - `ACC_atmp_`
  - `MILL1`
  - `MILL2`
  - `MILL3`
  - `MILL4`
  - `MILL`
  - `DECL13`
  - `M13_A`
  - `M13_A_`
  - `M13_A_0_0`
  - `M13_A_0_1`
  - `M13_A_0_2`
  - `M13_A_0_3`
  - `M13_A_0_4`
  - `M13_A_0_5`
  - `M13_A_0_6`
  - `M13_A_0_7`
  - `M13_A_0_8`
  - `M13_A_0_9`
  - `M13_A_0_10`
  - `M13_A_0_11`
  - `M13_A_0_12`
  - `M13_A_1_0`
  - `M13_A_1_1`
  - `M13_A_1_2`
  - `M13_A_1_3`
  - `M13_A_1_4`
  - `M13_A_1_5`
  - `M13_A_1_6`
  - `M13_A_1_7`
  - `M13_A_1_8`
  - `M13_A_1_9`
  - `M13_A_1_10`
  - `M13_A_1_11`
  - `M13_A_1_12`
  - `M13_A_2_0`
  - `M13_A_2_1`
  - `M13_A_2_2`
  - `M13_A_2_3`
  - `M13_A_2_4`
  - `M13_A_2_5`
  - `M13_A_2_6`
  - `M13_A_2_7`
  - `M13_A_2_8`
  - `M13_A_2_9`
  - `M13_A_2_10`
  - `M13_A_2_11`
  - `M13_A_2_12`
  - `M13_A_3_0`
  - `M13_A_3_1`
  - `M13_A_3_2`
  - `M13_A_3_3`
  - `M13_A_3_4`
  - `M13_A_3_5`
  - `M13_A_3_6`
  - `M13_A_3_7`
  - `M13_A_3_8`
  - `M13_A_3_9`
  - `M13_A_3_10`
  - `M13_A_3_11`
  - `M13_A_3_12`
  - `M13_A_4_0`
  - `M13_A_4_1`
  - `M13_A_4_2`
  - `M13_A_4_3`
  - `M13_A_4_4`
  - `M13_A_4_5`
  - `M13_A_4_6`
  - `M13_A_4_7`
  - `M13_A_4_8`
  - `M13_A_4_9`
  - `M13_A_4_10`
  - `M13_A_4_11`
  - `M13_A_4_12`
  - `M13_A_5_0`
  - `M13_A_5_1`
  - `M13_A_5_2`
  - `M13_A_5_3`
  - `M13_A_5_4`
  - `M13_A_5_5`
  - `M13_A_5_6`
  - `M13_A_5_7`
  - `M13_A_5_8`
  - `M13_A_5_9`
  - `M13_A_5_10`
  - `M13_A_5_11`
  - `M13_A_5_12`
  - `M13_A_6_0`
  - `M13_A_6_1`
  - `M13_A_6_2`
  - `M13_A_6_3`
  - `M13_A_6_4`
  - `M13_A_6_5`
  - `M13_A_6_6`
  - `M13_A_6_7`
  - `M13_A_6_8`
  - `M13_A_6_9`
  - `M13_A_6_10`
  - `M13_A_6_11`
  - `M13_A_6_12`
  - `M13_A_7_0`
  - `M13_A_7_1`
  - `M13_A_7_2`
  - `M13_A_7_3`
  - `M13_A_7_4`
  - `M13_A_7_5`
  - `M13_A_7_6`
  - `M13_A_7_7`
  - `M13_A_7_8`
  - `M13_A_7_9`
  - `M13_A_7_10`
  - `M13_A_7_11`
  - `M13_A_7_12`
  - `M13_A_8_0`
  - `M13_A_8_1`
  - `M13_A_8_2`
  - `M13_A_8_3`
  - `M13_A_8_4`
  - `M13_A_8_5`
  - `M13_A_8_6`
  - `M13_A_8_7`
  - `M13_A_8_8`
  - `M13_A_8_9`
  - `M13_A_8_10`
  - `M13_A_8_11`
  - `M13_A_8_12`
  - `M13_A_9_0`
  - `M13_A_9_1`
  - `M13_A_9_2`
  - `M13_A_9_3`
  - `M13_A_9_4`
  - `M13_A_9_5`
  - `M13_A_9_6`
  - `M13_A_9_7`
  - `M13_A_9_8`
  - `M13_A_9_9`
  - `M13_A_9_10`
  - `M13_A_9_11`
  - `M13_A_9_12`
  - `M13_A_10_0`
  - `M13_A_10_1`
  - `M13_A_10_2`
  - `M13_A_10_3`
  - `M13_A_10_4`
  - `M13_A_10_5`
  - `M13_A_10_6`
  - `M13_A_10_7`
  - `M13_A_10_8`
  - `M13_A_10_9`
  - `M13_A_10_10`
  - `M13_A_10_11`
  - `M13_A_10_12`
  - `M13_A_11_0`
  - `M13_A_11_1`
  - `M13_A_11_2`
  - `M13_A_11_3`
  - `M13_A_11_4`
  - `M13_A_11_5`
  - `M13_A_11_6`
  - `M13_A_11_7`
  - `M13_A_11_8`
  - `M13_A_11_9`
  - `M13_A_11_10`
  - `M13_A_11_11`
  - `M13_A_11_12`
  - `M13_A_12_0`
  - `M13_A_12_1`
  - `M13_A_12_2`
  - `M13_A_12_3`
  - `M13_A_12_4`
  - `M13_A_12_5`
  - `M13_A_12_6`
  - `M13_A_12_7`
  - `M13_A_12_8`
  - `M13_A_12_9`
  - `M13_A_12_10`
  - `M13_A_12_11`
  - `M13_A_12_12`
  - `M13_N`
  - `M13_N_`
  - `M13_N_0`
  - `M13_N_1`
  - `M13_N_2`
  - `M13_N_3`
  - `M13_N_4`
  - `M13_N_5`
  - `M13_N_6`
  - `M13_N_7`
  - `M13_N_8`
  - `M13_N_9`
  - `M13_N_10`
  - `M13_N_11`
  - `M13_N_12`
  - `ACC_b`
  - `ACC_b_`
  - `ROUND_ELT`
  - `ROUND_SF`
  - `INPUT_SF`
  - `ROUND`
  - `INPUT`
  - `MUL13`
  - `MILL_READ_ELT`
  - `MILL_WRITE_ELT`
  - `STATE_READ_SF`
  - `STATE_WRITE_SF`
  - `PUSH13_SF`
  - `STATE_READ`
  - `STATE_WRITE`
  - `PUSH13`
  - `BELT_READ_ELT`
  - `BELT_WRITE_ELT`
  - `PUSH13_ELT`
  - `BLANK13_SF`
  - `BLANK1_SF`
  - `BLANK13`
  - `BLANK1`
  - `BLANK13_ELT`
  - `MUL12`
  - `BLANK1_ELT`
  - `NO_TOKEN`
  - `CLOSE_SF`
  - `CLOSE`
  - `CLOSE_GEN`
  - `INIT`
  - `WT`
  - `T`
  - `ROR`
  - `INW`
  - `OUTW`

### sha3/sph_radiogatun.h
- Functions: sph_radiogatun32_init, sph_radiogatun32, sph_radiogatun32_close, sph_radiogatun64_init, sph_radiogatun64, sph_radiogatun64_close
- Macros: SPH_RADIOGATUN_H__, SPH_SIZE_radiogatun32, SPH_SIZE_radiogatun64

### sha3/sph_ripemd.c
- Functions: ripemd_round, sph_ripemd_init, sph_ripemd_close, sph_ripemd_comp, ripemd128_round, sph_ripemd128_init, sph_ripemd128_close, sph_ripemd128_comp, ripemd160_round, sph_ripemd160_init, sph_ripemd160_close, sph_ripemd160_comp
- Macros: F, G, H, F1, F2, F3, F4, F5, ROTL, FF1, GG1, HH1, FF2, GG2, HH2, RIPEMD_ROUND_BODY, RIPEMD_IN, RFUN, HASH, LE32, sK11, sK12, sK13, sK14, sK21, sK22, sK23, sK24, sRR, sROUND1, sROUND2, RIPEMD128_ROUND_BODY, RIPEMD128_IN, K11, K12, K13, K14, K15, K21, K22, K23, K24, K25, RR, ROUND1, ROUND2, RIPEMD160_ROUND_BODY, RIPEMD160_IN

### sha3/sph_ripemd.h
- Functions: sph_ripemd_init, sph_ripemd, sph_ripemd_close, sph_ripemd_comp, sph_ripemd128_init, sph_ripemd128, sph_ripemd128_close, sph_ripemd128_comp, sph_ripemd160_init, sph_ripemd160, sph_ripemd160_close, sph_ripemd160_comp
- Macros: SPH_RIPEMD_H__, SPH_SIZE_ripemd, SPH_SIZE_ripemd128, SPH_SIZE_ripemd160

### sha3/sph_sha2.c
- Functions: sha2_round, sph_sha224_init, sph_sha256_init, sph_sha224_close, sph_sha224_addbits_and_close, sph_sha256_close, sph_sha256_addbits_and_close, sph_sha224_comp
- Macros: SPH_SMALL_FOOTPRINT_SHA2, CH, MAJ, ROTR, BSG2_0, BSG2_1, SSG2_0, SSG2_1, SHA2_MEXP1, SHA2_MEXP2, SHA2_STEPn, SHA2_STEP1, SHA2_STEP2, SHA2_ROUND_BODY, SHA2_IN, RFUN, HASH, BE32

### sha3/sph_sha2.h
- Functions: sph_sha224_init, sph_sha224, sph_sha224_close, sph_sha224_addbits_and_close, sph_sha224_comp, sph_sha256_init, sph_sha256, sph_sha256_close, sph_sha256_addbits_and_close, sph_sha256_comp, sph_sha384_init, sph_sha384, sph_sha384_close, sph_sha384_addbits_and_close, sph_sha384_comp, sph_sha512_init, sph_sha512, sph_sha512_close, sph_sha512_addbits_and_close, sph_sha512_comp
- Macros: SPH_SHA2_H__, SPH_SIZE_sha224, SPH_SIZE_sha256, sph_sha256, sph_sha256_comp, SPH_SIZE_sha384, SPH_SIZE_sha512, sph_sha512, sph_sha512_comp

### sha3/sph_sha2big.c
- Functions: sha3_round, sph_sha384_init, sph_sha512_init, sph_sha384_close, sph_sha384_addbits_and_close, sph_sha512_close, sph_sha512_addbits_and_close, sph_sha384_comp
- Macros: CH, MAJ, ROTR64, BSG5_0, BSG5_1, SSG5_0, SSG5_1, SHA3_STEP, SHA3_ROUND_BODY, SHA3_IN, RFUN, HASH, BE64

### sha3/sph_shabal.c
- Functions: shabal_init, shabal_core, shabal_close, sph_shabal192_init, sph_shabal192, sph_shabal192_close, sph_shabal192_addbits_and_close, sph_shabal224_init, sph_shabal224, sph_shabal224_close, sph_shabal224_addbits_and_close, sph_shabal256_init, sph_shabal256, sph_shabal256_close, sph_shabal256_addbits_and_close, sph_shabal384_init, sph_shabal384, sph_shabal384_close, sph_shabal384_addbits_and_close, sph_shabal512_init, sph_shabal512, sph_shabal512_close, sph_shabal512_addbits_and_close
- Macros: sM, C32, T32, O1, O2, O3, DECL_STATE, READ_STATE, WRITE_STATE, DECODE_BLOCK, INPUT_BLOCK_ADD, INPUT_BLOCK_SUB, XOR_W, SWAP, SWAP_BC, PERM_ELT, PERM_STEP_0, PERM_STEP_1, PERM_STEP_2, APPLY_P, INCR_W

### sha3/sph_shabal.h
- Functions: sph_shabal192_init, sph_shabal192, sph_shabal192_close, sph_shabal192_addbits_and_close, sph_shabal224_init, sph_shabal224, sph_shabal224_close, sph_shabal224_addbits_and_close, sph_shabal256_init, sph_shabal256, sph_shabal256_close, sph_shabal256_addbits_and_close, sph_shabal384_init, sph_shabal384, sph_shabal384_close, sph_shabal384_addbits_and_close, sph_shabal512_init, sph_shabal512, sph_shabal512_close, sph_shabal512_addbits_and_close
- Macros: SPH_SHABAL_H__, SPH_SIZE_shabal192, SPH_SIZE_shabal224, SPH_SIZE_shabal256, SPH_SIZE_shabal384, SPH_SIZE_shabal512

### sha3/sph_shavite.c
- Functions: c256, c512, shavite_small_init, shavite_small_core, shavite_small_close, shavite_big_init, shavite_big_core, shavite_big_close, sph_shavite224_init, sph_shavite224, sph_shavite224_close, sph_shavite224_addbits_and_close, sph_shavite256_init, sph_shavite256, sph_shavite256_close, sph_shavite256_addbits_and_close, sph_shavite384_init, sph_shavite384, sph_shavite384_close, sph_shavite384_addbits_and_close, sph_shavite512_init, sph_shavite512, sph_shavite512_close, sph_shavite512_addbits_and_close
- Macros: SPH_SMALL_FOOTPRINT_SHAVITE, C32, AES_BIG_ENDIAN, AES_ROUND_NOKEY, KEY_EXPAND_ELT, C512_ELT, WROT

### sha3/sph_shavite.h
- Functions: sph_shavite224_init, sph_shavite224, sph_shavite224_close, sph_shavite224_addbits_and_close, sph_shavite256_init, sph_shavite256, sph_shavite256_close, sph_shavite256_addbits_and_close, sph_shavite384_init, sph_shavite384, sph_shavite384_close, sph_shavite384_addbits_and_close, sph_shavite512_init, sph_shavite512, sph_shavite512_close, sph_shavite512_addbits_and_close
- Macros: SPH_SHAVITE_H__, SPH_SIZE_shavite224, SPH_SIZE_shavite256, SPH_SIZE_shavite384, SPH_SIZE_shavite512

### sha3/sph_simd.c
- Functions: fft32, fft64, one_round_small, compress_small, one_round_big, compress_big, init_small, init_big, update_small, update_big, encode_count_small, encode_count_big, finalize_small, finalize_big, sph_simd224_init, sph_simd224, sph_simd224_close, sph_simd224_addbits_and_close, sph_simd256_init, sph_simd256, sph_simd256_close, sph_simd256_addbits_and_close, sph_simd384_init, sph_simd384, sph_simd384_close, sph_simd384_addbits_and_close, sph_simd512_init, sph_simd512, sph_simd512_close, sph_simd512_addbits_and_close
- Macros:
  - `SPH_SMALL_FOOTPRINT_SIMD`
  - `C32`
  - `T32`
  - `ROL32`
  - `XCAT`
  - `XCAT_`
  - `REDS1`
  - `REDS2`
  - `FFT_LOOP`
  - `FFT8`
  - `FFT16`
  - `FFT32`
  - `FFT64`
  - `FFT128`
  - `FFT256`
  - `INNER`
  - `W_SMALL`
  - `WS_0_0`
  - `WS_0_1`
  - `WS_0_2`
  - `WS_0_3`
  - `WS_0_4`
  - `WS_0_5`
  - `WS_0_6`
  - `WS_0_7`
  - `WS_1_0`
  - `WS_1_1`
  - `WS_1_2`
  - `WS_1_3`
  - `WS_1_4`
  - `WS_1_5`
  - `WS_1_6`
  - `WS_1_7`
  - `WS_2_0`
  - `WS_2_1`
  - `WS_2_2`
  - `WS_2_3`
  - `WS_2_4`
  - `WS_2_5`
  - `WS_2_6`
  - `WS_2_7`
  - `WS_3_0`
  - `WS_3_1`
  - `WS_3_2`
  - `WS_3_3`
  - `WS_3_4`
  - `WS_3_5`
  - `WS_3_6`
  - `WS_3_7`
  - `W_BIG`
  - `WB_0_0`
  - `WB_0_1`
  - `WB_0_2`
  - `WB_0_3`
  - `WB_0_4`
  - `WB_0_5`
  - `WB_0_6`
  - `WB_0_7`
  - `WB_1_0`
  - `WB_1_1`
  - `WB_1_2`
  - `WB_1_3`
  - `WB_1_4`
  - `WB_1_5`
  - `WB_1_6`
  - `WB_1_7`
  - `WB_2_0`
  - `WB_2_1`
  - `WB_2_2`
  - `WB_2_3`
  - `WB_2_4`
  - `WB_2_5`
  - `WB_2_6`
  - `WB_2_7`
  - `WB_3_0`
  - `WB_3_1`
  - `WB_3_2`
  - `WB_3_3`
  - `WB_3_4`
  - `WB_3_5`
  - `WB_3_6`
  - `WB_3_7`
  - `IF`
  - `MAJ`
  - `PP4_0_0`
  - `PP4_0_1`
  - `PP4_0_2`
  - `PP4_0_3`
  - `PP4_1_0`
  - `PP4_1_1`
  - `PP4_1_2`
  - `PP4_1_3`
  - `PP4_2_0`
  - `PP4_2_1`
  - `PP4_2_2`
  - `PP4_2_3`
  - `PP8_0_0`
  - `PP8_0_1`
  - `PP8_0_2`
  - `PP8_0_3`
  - `PP8_0_4`
  - `PP8_0_5`
  - `PP8_0_6`
  - `PP8_0_7`
  - `PP8_1_0`
  - `PP8_1_1`
  - `PP8_1_2`
  - `PP8_1_3`
  - `PP8_1_4`
  - `PP8_1_5`
  - `PP8_1_6`
  - `PP8_1_7`
  - `PP8_2_0`
  - `PP8_2_1`
  - `PP8_2_2`
  - `PP8_2_3`
  - `PP8_2_4`
  - `PP8_2_5`
  - `PP8_2_6`
  - `PP8_2_7`
  - `PP8_3_0`
  - `PP8_3_1`
  - `PP8_3_2`
  - `PP8_3_3`
  - `PP8_3_4`
  - `PP8_3_5`
  - `PP8_3_6`
  - `PP8_3_7`
  - `PP8_4_0`
  - `PP8_4_1`
  - `PP8_4_2`
  - `PP8_4_3`
  - `PP8_4_4`
  - `PP8_4_5`
  - `PP8_4_6`
  - `PP8_4_7`
  - `PP8_5_0`
  - `PP8_5_1`
  - `PP8_5_2`
  - `PP8_5_3`
  - `PP8_5_4`
  - `PP8_5_5`
  - `PP8_5_6`
  - `PP8_5_7`
  - `PP8_6_0`
  - `PP8_6_1`
  - `PP8_6_2`
  - `PP8_6_3`
  - `PP8_6_4`
  - `PP8_6_5`
  - `PP8_6_6`
  - `PP8_6_7`
  - `DECL_STATE_SMALL`
  - `READ_STATE_SMALL`
  - `WRITE_STATE_SMALL`
  - `DECL_STATE_BIG`
  - `READ_STATE_BIG`
  - `WRITE_STATE_BIG`
  - `STEP_ELT`
  - `STEP_SMALL`
  - `STEP_BIG`
  - `M3_0_0`
  - `M3_1_0`
  - `M3_2_0`
  - `M3_3_0`
  - `M3_4_0`
  - `M3_5_0`
  - `M3_6_0`
  - `M3_7_0`
  - `M3_0_1`
  - `M3_1_1`
  - `M3_2_1`
  - `M3_3_1`
  - `M3_4_1`
  - `M3_5_1`
  - `M3_6_1`
  - `M3_7_1`
  - `M3_0_2`
  - `M3_1_2`
  - `M3_2_2`
  - `M3_3_2`
  - `M3_4_2`
  - `M3_5_2`
  - `M3_6_2`
  - `M3_7_2`
  - `STEP_SMALL_`
  - `ONE_ROUND_SMALL`
  - `M7_0_0`
  - `M7_1_0`
  - `M7_2_0`
  - `M7_3_0`
  - `M7_4_0`
  - `M7_5_0`
  - `M7_6_0`
  - `M7_7_0`
  - `M7_0_1`
  - `M7_1_1`
  - `M7_2_1`
  - `M7_3_1`
  - `M7_4_1`
  - `M7_5_1`
  - `M7_6_1`
  - `M7_7_1`
  - `M7_0_2`
  - `M7_1_2`
  - `M7_2_2`
  - `M7_3_2`
  - `M7_4_2`
  - `M7_5_2`
  - `M7_6_2`
  - `M7_7_2`
  - `M7_0_3`
  - `M7_1_3`
  - `M7_2_3`
  - `M7_3_3`
  - `M7_4_3`
  - `M7_5_3`
  - `M7_6_3`
  - `M7_7_3`
  - `STEP_BIG_`
  - `ONE_ROUND_BIG`
  - `A0`
  - `A1`
  - `A2`
  - `A3`
  - `B0`
  - `B1`
  - `B2`
  - `B3`
  - `C0`
  - `C1`
  - `C2`
  - `C3`
  - `D0`
  - `D1`
  - `D2`
  - `D3`
  - `STEP2_ELT`
  - `STEP2_SMALL`
  - `WSREAD`
  - `A4`
  - `A5`
  - `A6`
  - `A7`
  - `B4`
  - `B5`
  - `B6`
  - `B7`
  - `C4`
  - `C5`
  - `C6`
  - `C7`
  - `D4`
  - `D5`
  - `D6`
  - `D7`
  - `STEP2_BIG`
  - `WBREAD`

### sha3/sph_simd.h
- Functions: sph_simd224_init, sph_simd224, sph_simd224_close, sph_simd224_addbits_and_close, sph_simd256_init, sph_simd256, sph_simd256_close, sph_simd256_addbits_and_close, sph_simd384_init, sph_simd384, sph_simd384_close, sph_simd384_addbits_and_close, sph_simd512_init, sph_simd512, sph_simd512_close, sph_simd512_addbits_and_close
- Macros: SPH_SIMD_H__, SPH_SIZE_simd224, SPH_SIZE_simd256, SPH_SIZE_simd384, SPH_SIZE_simd512

### sha3/sph_skein.c
- Functions: skein_small_init, skein_big_init, skein_small_core, skein_big_core, skein_small_close, skein_big_close, sph_skein224_init, sph_skein224, sph_skein224_close, sph_skein224_addbits_and_close, sph_skein256_init, sph_skein256, sph_skein256_close, sph_skein256_addbits_and_close, sph_skein384_init, sph_skein384, sph_skein384_close, sph_skein384_addbits_and_close, sph_skein512_init, sph_skein512, sph_skein512_close, sph_skein512_addbits_and_close
- Macros:
  - `SPH_SMALL_FOOTPRINT_SKEIN`
  - `M5_0_0`
  - `M5_0_1`
  - `M5_0_2`
  - `M5_0_3`
  - `M5_1_0`
  - `M5_1_1`
  - `M5_1_2`
  - `M5_1_3`
  - `M5_2_0`
  - `M5_2_1`
  - `M5_2_2`
  - `M5_2_3`
  - `M5_3_0`
  - `M5_3_1`
  - `M5_3_2`
  - `M5_3_3`
  - `M5_4_0`
  - `M5_4_1`
  - `M5_4_2`
  - `M5_4_3`
  - `M5_5_0`
  - `M5_5_1`
  - `M5_5_2`
  - `M5_5_3`
  - `M5_6_0`
  - `M5_6_1`
  - `M5_6_2`
  - `M5_6_3`
  - `M5_7_0`
  - `M5_7_1`
  - `M5_7_2`
  - `M5_7_3`
  - `M5_8_0`
  - `M5_8_1`
  - `M5_8_2`
  - `M5_8_3`
  - `M5_9_0`
  - `M5_9_1`
  - `M5_9_2`
  - `M5_9_3`
  - `M5_10_0`
  - `M5_10_1`
  - `M5_10_2`
  - `M5_10_3`
  - `M5_11_0`
  - `M5_11_1`
  - `M5_11_2`
  - `M5_11_3`
  - `M5_12_0`
  - `M5_12_1`
  - `M5_12_2`
  - `M5_12_3`
  - `M5_13_0`
  - `M5_13_1`
  - `M5_13_2`
  - `M5_13_3`
  - `M5_14_0`
  - `M5_14_1`
  - `M5_14_2`
  - `M5_14_3`
  - `M5_15_0`
  - `M5_15_1`
  - `M5_15_2`
  - `M5_15_3`
  - `M5_16_0`
  - `M5_16_1`
  - `M5_16_2`
  - `M5_16_3`
  - `M5_17_0`
  - `M5_17_1`
  - `M5_17_2`
  - `M5_17_3`
  - `M5_18_0`
  - `M5_18_1`
  - `M5_18_2`
  - `M5_18_3`
  - `M9_0_0`
  - `M9_0_1`
  - `M9_0_2`
  - `M9_0_3`
  - `M9_0_4`
  - `M9_0_5`
  - `M9_0_6`
  - `M9_0_7`
  - `M9_1_0`
  - `M9_1_1`
  - `M9_1_2`
  - `M9_1_3`
  - `M9_1_4`
  - `M9_1_5`
  - `M9_1_6`
  - `M9_1_7`
  - `M9_2_0`
  - `M9_2_1`
  - `M9_2_2`
  - `M9_2_3`
  - `M9_2_4`
  - `M9_2_5`
  - `M9_2_6`
  - `M9_2_7`
  - `M9_3_0`
  - `M9_3_1`
  - `M9_3_2`
  - `M9_3_3`
  - `M9_3_4`
  - `M9_3_5`
  - `M9_3_6`
  - `M9_3_7`
  - `M9_4_0`
  - `M9_4_1`
  - `M9_4_2`
  - `M9_4_3`
  - `M9_4_4`
  - `M9_4_5`
  - `M9_4_6`
  - `M9_4_7`
  - `M9_5_0`
  - `M9_5_1`
  - `M9_5_2`
  - `M9_5_3`
  - `M9_5_4`
  - `M9_5_5`
  - `M9_5_6`
  - `M9_5_7`
  - `M9_6_0`
  - `M9_6_1`
  - `M9_6_2`
  - `M9_6_3`
  - `M9_6_4`
  - `M9_6_5`
  - `M9_6_6`
  - `M9_6_7`
  - `M9_7_0`
  - `M9_7_1`
  - `M9_7_2`
  - `M9_7_3`
  - `M9_7_4`
  - `M9_7_5`
  - `M9_7_6`
  - `M9_7_7`
  - `M9_8_0`
  - `M9_8_1`
  - `M9_8_2`
  - `M9_8_3`
  - `M9_8_4`
  - `M9_8_5`
  - `M9_8_6`
  - `M9_8_7`
  - `M9_9_0`
  - `M9_9_1`
  - `M9_9_2`
  - `M9_9_3`
  - `M9_9_4`
  - `M9_9_5`
  - `M9_9_6`
  - `M9_9_7`
  - `M9_10_0`
  - `M9_10_1`
  - `M9_10_2`
  - `M9_10_3`
  - `M9_10_4`
  - `M9_10_5`
  - `M9_10_6`
  - `M9_10_7`
  - `M9_11_0`
  - `M9_11_1`
  - `M9_11_2`
  - `M9_11_3`
  - `M9_11_4`
  - `M9_11_5`
  - `M9_11_6`
  - `M9_11_7`
  - `M9_12_0`
  - `M9_12_1`
  - `M9_12_2`
  - `M9_12_3`
  - `M9_12_4`
  - `M9_12_5`
  - `M9_12_6`
  - `M9_12_7`
  - `M9_13_0`
  - `M9_13_1`
  - `M9_13_2`
  - `M9_13_3`
  - `M9_13_4`
  - `M9_13_5`
  - `M9_13_6`
  - `M9_13_7`
  - `M9_14_0`
  - `M9_14_1`
  - `M9_14_2`
  - `M9_14_3`
  - `M9_14_4`
  - `M9_14_5`
  - `M9_14_6`
  - `M9_14_7`
  - `M9_15_0`
  - `M9_15_1`
  - `M9_15_2`
  - `M9_15_3`
  - `M9_15_4`
  - `M9_15_5`
  - `M9_15_6`
  - `M9_15_7`
  - `M9_16_0`
  - `M9_16_1`
  - `M9_16_2`
  - `M9_16_3`
  - `M9_16_4`
  - `M9_16_5`
  - `M9_16_6`
  - `M9_16_7`
  - `M9_17_0`
  - `M9_17_1`
  - `M9_17_2`
  - `M9_17_3`
  - `M9_17_4`
  - `M9_17_5`
  - `M9_17_6`
  - `M9_17_7`
  - `M9_18_0`
  - `M9_18_1`
  - `M9_18_2`
  - `M9_18_3`
  - `M9_18_4`
  - `M9_18_5`
  - `M9_18_6`
  - `M9_18_7`
  - `M3_0_0`
  - `M3_0_1`
  - `M3_1_0`
  - `M3_1_1`
  - `M3_2_0`
  - `M3_2_1`
  - `M3_3_0`
  - `M3_3_1`
  - `M3_4_0`
  - `M3_4_1`
  - `M3_5_0`
  - `M3_5_1`
  - `M3_6_0`
  - `M3_6_1`
  - `M3_7_0`
  - `M3_7_1`
  - `M3_8_0`
  - `M3_8_1`
  - `M3_9_0`
  - `M3_9_1`
  - `M3_10_0`
  - `M3_10_1`
  - `M3_11_0`
  - `M3_11_1`
  - `M3_12_0`
  - `M3_12_1`
  - `M3_13_0`
  - `M3_13_1`
  - `M3_14_0`
  - `M3_14_1`
  - `M3_15_0`
  - `M3_15_1`
  - `M3_16_0`
  - `M3_16_1`
  - `M3_17_0`
  - `M3_17_1`
  - `M3_18_0`
  - `M3_18_1`
  - `XCAT`
  - `XCAT_`
  - `SKSI`
  - `SKST`
  - `SKBI`
  - `SKBT`
  - `TFSMALL_KINIT`
  - `TFBIG_KINIT`
  - `TFSMALL_ADDKEY`
  - `TFBIG_ADDKEY`
  - `TFSMALL_MIX`
  - `TFBIG_MIX`
  - `TFSMALL_MIX4`
  - `TFBIG_MIX8`
  - `TFSMALL_4e`
  - `TFSMALL_4o`
  - `TFBIG_4e`
  - `TFBIG_4o`
  - `UBI_SMALL`
  - `UBI_BIG`
  - `DECL_STATE_SMALL`
  - `READ_STATE_SMALL`
  - `WRITE_STATE_SMALL`
  - `DECL_STATE_BIG`
  - `READ_STATE_BIG`
  - `WRITE_STATE_BIG`

### sha3/sph_skein.h
- Functions: sph_skein224_init, sph_skein224, sph_skein224_close, sph_skein224_addbits_and_close, sph_skein256_init, sph_skein256, sph_skein256_close, sph_skein256_addbits_and_close, sph_skein384_init, sph_skein384, sph_skein384_close, sph_skein384_addbits_and_close, sph_skein512_init, sph_skein512, sph_skein512_close, sph_skein512_addbits_and_close
- Macros: SPH_SKEIN_H__, SPH_SIZE_skein224, SPH_SIZE_skein256, SPH_SIZE_skein384, SPH_SIZE_skein512

### sha3/sph_tiger.c
- Functions: tiger_round, sph_tiger_init, sph_tiger_close, sph_tiger_comp, sph_tiger2_close
- Macros: PASS, ROUND, MUL5, MUL7, MUL9, KSCHED, TIGER_ROUND_BODY, TIGER_IN, RFUN, HASH, LE64, BLEN, PW01, PLW1, CLOSE_ONLY

### sha3/sph_tiger.h
- Functions: sph_tiger_init, sph_tiger, sph_tiger_close, sph_tiger_comp, sph_tiger2_init, sph_tiger2, sph_tiger2_close, sph_tiger2_comp
- Macros: SPH_TIGER_H__, SPH_SIZE_tiger, SPH_SIZE_tiger2, sph_tiger2_init, sph_tiger2, sph_tiger2_comp

### sha3/sph_types.h
- Functions: sph_bswap32, sph_bswap64, sph_dec16le, sph_enc16le, sph_dec16be, sph_enc16be, sph_dec32le, sph_dec32le_aligned, sph_enc32le, sph_enc32le_aligned, sph_dec32be, sph_dec32be_aligned, sph_enc32be, sph_enc32be_aligned, sph_dec64le, sph_dec64le_aligned, sph_enc64le, sph_enc64le_aligned, sph_dec64be, sph_dec64be_aligned, sph_enc64be, sph_enc64be_aligned, __volatile__, __declspec
- Macros:
  - `SPH_TYPES_H__`
  - `SPH_C32`
  - `SPH_T32`
  - `SPH_ROTL32`
  - `SPH_ROTR32`
  - `SPH_64`
  - `SPH_64_TRUE`
  - `SPH_C64`
  - `SPH_T64`
  - `SPH_ROTL64`
  - `SPH_ROTR64`
  - `SPH_INLINE`
  - `SPH_LITTLE_ENDIAN`
  - `SPH_BIG_ENDIAN`
  - `SPH_LITTLE_FAST`
  - `SPH_BIG_FAST`
  - `SPH_UPTR`
  - `SPH_UNALIGNED`
  - `SPH_DETECT_UNALIGNED`
  - `SPH_DETECT_LITTLE_ENDIAN`
  - `SPH_DETECT_UPTR`
  - `SPH_DETECT_I386_GCC`
  - `SPH_DETECT_I386_MSVC`
  - `SPH_DETECT_AMD64_GCC`
  - `SPH_DETECT_AMD64_MSVC`
  - `SPH_DETECT_BIG_ENDIAN`
  - `SPH_DETECT_SPARCV9_GCC_64`
  - `SPH_DETECT_LITTLE_FAST`
  - `SPH_DETECT_SPARCV9_GCC_32`
  - `SPH_DETECT_PPC64_GCC`
  - `SPH_DETECT_PPC32_GCC`
  - `SPH_DETECT_SPARCV9_GCC`
  - `SPH_SPARCV9_GCC_32`
  - `SPH_SPARCV9_GCC_64`
  - `SPH_SPARCV9_GCC`
  - `SPH_I386_GCC`
  - `SPH_I386_MSVC`
  - `SPH_AMD64_GCC`
  - `SPH_AMD64_MSVC`
  - `SPH_PPC32_GCC`
  - `SPH_PPC64_GCC`
  - `SPH_SPARCV9_SET_ASI`
  - `SPH_SPARCV9_RESET_ASI`
  - `SPH_SPARCV9_DEC32LE`

### sha3/sph_whirlpool.c
- Functions: table_skew, SPH_ROTL64, sph_whirlpool_init
- Macros: SPH_SMALL_FOOTPRINT_WHIRLPOOL, DECL8, READ_DATA_W, UPDATE_STATE_W, LVARS, READ_STATE_W, MUL8, ROUND0_W, READ_DATA, READ_STATE, ROUND0, UPDATE_STATE, BYTE, ROUND_ELT, ROUND, ROUND_KSCHED, ROUND_WENC, TRANSFER, ROUND_FUN, BE64, SVAL, BLEN, PLW4, RFUN, HASH, MAKE_CLOSE

### sha3/sph_whirlpool.h
- Functions: sph_whirlpool_init, sph_whirlpool, sph_whirlpool_close, sph_whirlpool0_init, sph_whirlpool0, sph_whirlpool0_close, sph_whirlpool1_init, sph_whirlpool1, sph_whirlpool1_close
- Macros: SPH_WHIRLPOOL_H__, SPH_SIZE_whirlpool, SPH_SIZE_whirlpool0, SPH_SIZE_whirlpool1, sph_whirlpool0_init, sph_whirlpool1_init

### sysinfos.c
- Functions: linux_cputemp, linux_cpufreq, win32_cputemp, cpu_temp, cpu_clock, cpu_fanpercent, cpuid, volatile, cpu_getname, cpu_getmodelid, has_aes_ni, cpu_bestfeature
- Macros: HWMON_PATH, HWMON_ALT, HWMON_ALT2, HWMON_ALT3, HWMON_ALT4, HWMON_ALT5, HWMON_ALT6, CPUFREQ_PATH, cpuid, OSXSAVE_Flag, AVX1_Flag, XOP_Flag, FMA3_Flag, AES_Flag, SSE42_Flag, SSE_Flag, SSE2_Flag, AVX2_Flag

### uint256.h
- Functions: Testuint256AdHoc, a, SetHex, begin, end, Unserialize, uint160, uint256, g, k
- Macros: BITCOIN_UINT256_H

### util.c
- Functions:
  - `applog`
  - `get_defconfig_path`
  - `format_hashrate`
  - `databuf_free`
  - `all_data_cb`
  - `upload_data_cb`
  - `seek_data_cb`
  - `resp_hdr_cb`
  - `sockopt_keepalive_cb`
  - `json_load_url`
  - `curl_easy_setopt`
  - `bin2hex`
  - `hex2bin`
  - `varint_encode`
  - `b58dec`
  - `b58check`
  - `jobj_binary`
  - `address_to_script`
  - `timeval_subtract`
  - `fulltest`
  - `diff_to_target`
  - `work_set_target`
  - `target_to_diff`
  - `send_line`
  - `stratum_send_line`
  - `socket_full`
  - `stratum_socket_full`
  - `strlen`
  - `stratum_buffer_append`
  - `opensocket_grab_cb`
  - `stratum_connect`
  - `stratum_disconnect`
  - `json_string_value`
  - `stratum_parse_extranonce`
  - `stratum_subscribe`
  - `stratum_authorize`
  - `rpc2_login_decode`
  - `json_rpc2_call_recur`
  - `rpc2_job_decode`
  - `getblocheight`
  - `stratum_notify`
  - `stratum_set_difficulty`
  - `stratum_reconnect`
  - `json_object_set_error`
  - `stratum_benchdata`
  - `stratum_get_stats`
  - `stratum_unknown_method`
  - `stratum_pong`
  - `stratum_get_algo`
  - `stratum_get_version`
  - `stratum_show_message`
  - `stratum_handle_method`
  - `tq_free`
  - `tq_freezethaw`
  - `tq_freeze`
  - `tq_thaw`
  - `tq_push`
  - `format_hash`
  - `applog_compare_hash`
  - `applog_hash`
  - `applog_hex`
  - `applog_hash64`
  - `print_hash_tests`
- Types: data_buffer, upload_buffer, header_info, tq_ent, list_head, thread_q, tm, stat, tcp_keepalive, curl_slist, timeval, work, stratum_ctx, curl_sockaddr, timespec
- Macros: _GNU_SOURCE, socket_blocks, RBUFSIZE, RECVSIZE, printpfx

### yescrypt/sha256_Y.c
- Functions: be32enc_vect, be32dec_vect, SHA256_Transform, SHA256_Pad, SHA256_Init_Y, SHA256_Update_Y, SHA256_Final_Y, HMAC_SHA256_Init_Y, HMAC_SHA256_Update_Y, HMAC_SHA256_Final_Y, PBKDF2_SHA256
- Macros: Ch, Maj, SHR, ROTR, S0, S1, s0, s1, RND, RNDr

### yescrypt/sha256_Y.h
- Functions: SHA256_Init_Y, SHA256_Update_Y, SHA256_Final_Y, HMAC_SHA256_Init_Y, HMAC_SHA256_Update_Y, HMAC_SHA256_Final_Y, PBKDF2_SHA256
- Types: SHA256Context, HMAC_SHA256Context
- Macros: _SHA256_H_

### yescrypt/sysendian.h
- Functions: be64dec, be64enc, le64dec, le64enc, be32dec, be32enc
- Macros: _SYSENDIAN_H_

### yescrypt/yescrypt-best.c
- No exported symbols detected; file provides local implementation details.

### yescrypt/yescrypt-common.c
- Functions: encode64_uint32, encode64, decode64_one, decode64_uint32, yescrypt_r, yescrypt, yescrypt_gensalt_r, yescrypt_gensalt, yescrypt_bsty, yescrypt_hash, yescrypt_hash_r8, yescrypt_hash_r16, yescrypt_hash_r32, yescrypthash
- Macros: BYTES2CHARS, HASH_SIZE, HASH_LEN, YESCRYPT_FLAGS

### yescrypt/yescrypt-opt.c
- Functions: blkcpy, blkxor, salsa20_simd_shuffle, salsa20_simd_unshuffle, salsa20_8, blockmix_salsa8, block_pwxform, blockmix_pwxform, integerify, smix1, smix2, p2floor, smix, yescrypt_kdf, HMAC_SHA256_Update_Y
- Macros: COMBINE, x, R, S_BITS, S_SIMD, S_P, S_ROUNDS, S_N, S_SIZE1, S_MASK, S_MASK2, S_SIZE_ALL, S_P_SIZE, S_MIN_R

### yescrypt/yescrypt-platform.h
- Functions: le32dec, le32enc, alloc_region, init_region, free_region, yescrypt_init_shared, yescrypt_free_shared, yescrypt_init_local, yescrypt_free_local
- Macros: HUGEPAGE_THRESHOLD, HUGEPAGE_SIZE

### yescrypt/yescrypt-simd.c
- Functions: blockmix_salsa8, blockmix, blockmix_salsa8_xor, _mm_cvtsi128_si32, blockmix_xor, blockmix_salsa8_xor_save, blockmix_xor_save, integerify, smix1, smix2, p2floor, smix, yescrypt_kdf
- Macros: restrict, PREFETCH, PREFETCH_OUT, ARX, SALSA20_2ROUNDS, SALSA20_8_BASE, SALSA20_8, SALSA20_8_XOR_ANY, SALSA20_8_XOR_MEM, SALSA20_8_XOR_REG, HI32, EXTRACT64, S_BITS, S_SIMD, S_P, S_N, S_SIZE1, S_MASK, S_MASK2, S_SIZE_ALL, PWXFORM_X_T, PWXFORM_SIMD, PWXFORM_ROUND, PWXFORM, XOR4, XOUT, XOR4_2, XOR4_Y

### yescrypt/yescrypt.h
- Functions: yescrypt_hash, yescrypt_hash_r8, yescrypt_hash_r16, yescrypt_hash_r32, crypto_scrypt, yescrypt_init_shared, yescrypt_free_shared, yescrypt_init_local, yescrypt_free_local, yescrypt_kdf, yescrypt_r, yescrypt, yescrypt_gensalt_r, yescrypt_gensalt
- Macros: YESCRYPT_H, YESCRYPT_KNOWN_FLAGS

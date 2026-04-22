#!/usr/bin/env python3
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = (ROOT / 'cpu-miner.c').read_text()


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


if __name__ == '__main__':
    test_bip34_reference_vectors()
    test_source_has_small_integer_fast_path()
    test_getblocktemplate_requests_advertise_segwit()
    print('ok')

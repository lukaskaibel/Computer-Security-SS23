import base64
import itertools
import hashlib
import sys
import secrets
from typing import Tuple


# Base 64 decode and perform OTP
def otp_decode(data: bytes, key: bytes):
    data = base64.b64decode(data)
    assert len(key) == 128
    assert len(data) == 128
    result = [a ^ b for a, b in itertools.zip_longest(key, data)]
    stripped = bytes(itertools.takewhile(lambda b: b != 0, result))
    return stripped


def generate_keys() -> Tuple[int, int]:
    # Generate a random 16-bit key
    k_0 = secrets.randbits(16)

    # Perform a 1-bit cyclic shift to the left
    # Use bitwise and with 0xFFFF to express that the resulting key definitely is within a 16-bit range.
    k_1 = ((k_0 >> 1) | (k_0 << 15)) & 0xFFFF

    print("Random Key:\n", format(k_0, "016b"))
    print("Shifted Key:\n", format(k_1, "016b"))
    return k_0, k_1


def generate_final_key() -> bytes:
    # 16-Bit keys
    k_0, k_1 = generate_keys()

    # As SHA-512 requires Byte-List instead of Bit-List, convert accordingly.
    k_0 = k_0.to_bytes(length=2, byteorder=sys.byteorder)
    k_1 = k_1.to_bytes(length=2, byteorder=sys.byteorder)

    # Compute the SHA-512 hashes
    h_0 = hashlib.sha512(k_0).digest()
    h_1 = hashlib.sha512(k_1).digest()
    print("SHA-512 of k_0:\n", h_0)
    print("SHA-512 of k_1:\n", h_1)

    # Concatenate hashes to get final key.
    key = h_0 + h_1
    return key

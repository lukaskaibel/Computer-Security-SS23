import hashlib
import itertools
import random
import secrets
import sys
import base64
import os

ciphertext_path = "Ciphertext"
plaintext_path = "plaintext"

def generate_keys() -> (int, int):
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


# Perform OTP and base 64 encode
def otp_encode(data: bytes, key: bytes):
    assert len(key) == 128
    assert len(data) <= 128
    result = bytes([a ^ b for a, b in itertools.zip_longest(key, data, fillvalue=0)])
    return base64.b64encode(result)


# Base 64 decode and perform OTP
def otp_decode(data: bytes, key: bytes):
    data = base64.b64decode(data)
    assert len(key) == 128
    assert len(data) == 128
    result = [a ^ b for a, b in itertools.zip_longest(key, data)]
    stripped = bytes(itertools.takewhile(lambda b: b!=0, result))
    return stripped


# Decode and write a txt file.
def write_text_file(filename: str, file_data: bytes):
    # Open the file in write text mode.
    with open(filename, "w") as file:
        file.write(file_data.decode("ascii"))

# Read and encode a txt file.
def read_text_file(filename: str) -> bytes:
    # Open the file in read text mode.
    with open(filename, "r") as file:
        plaintext = file.read()
    # Verify if all the characters are ASCII
    if all(ord(c) < 128 for c in plaintext):
        encoding = plaintext.encode("ascii")
        return encoding
    else:
        raise ValueError("Non-ASCII characters found in the input file.")

# Read n files from path {path}-{n}.txt
def read_n_texts(path: str, n: int) -> list:
    l = [0 for i in range(0, n)]
    for i in range(0, n):
        filename = "{p}-{n}.txt".format(p=path, n=i + 1)
        l[i] = read_text_file(filename)
    return l

# Shuffle the ciphertexts and write each to a separate file.
def write_ciphers_files(cts: list):
    random.shuffle(cts)
    for i in range(0, len(cts)):
        ct = cts[i]
        filename = "{p}-{n}.txt".format(p=ciphertext_path, n=i + 1)
        write_text_file(filename, ct)

# Write all keys to a single file.
def write_keys_file(keys: list):
    with open("keys.txt", "w") as file:
        for i, k in enumerate(keys, start=1):
            file.write(f"k_{i} = {k}\n")


if __name__ == "__main__":
    plaintexts = read_n_texts(plaintext_path, 13)
    keys = [generate_final_key() for i in range(0, 10)]
    write_keys_file(keys)

    # Encrypt m1...m7 with k1...k7.
    ciphertexts1 = [otp_encode(plaintexts[i], keys[i]) for i in range(0, 7)]
    # Re-encrypt m1..m3 with k8..k10.
    ciphertexts2 = [otp_encode(plaintexts[i], keys[7 + i]) for i in range(0, 3)]
    # Encrypt m8..m10 by reusing random keys from k1...k7
    ciphertexts3 = [
        otp_encode(plaintexts[i], keys[random.randint(0, 7)]) for i in range(7, 10)
    ]
    ciphertexts = ciphertexts1 + ciphertexts2 + ciphertexts3
    write_ciphers_files(ciphertexts)

    
    # Sanity checks

    # Check that we read the same ciphertext bytes as we wrote (in different order).
    ciphertexts_read = read_n_texts(ciphertext_path, 13)
    for ct in ciphertexts_read:
        ciphertexts.index(ct)

    # Check that we can decrypt the ciphertexts again.
    decrypted1 = [otp_decode(ciphertexts1[i], keys[i]) for i in range(0, 7)]
    assert decrypted1 == plaintexts[0:7]
    decrypted2 = [otp_decode(ciphertexts2[i], keys[7 + i]) for i in range(0, 3)]
    assert decrypted2 == plaintexts[0:3]
    for i in range(0, len(ciphertexts3)):
        # A random key was used, so we have to test each key if it works.
        for k in keys[0:7]:
            pt = otp_decode(ciphertexts3[i], k)
            if pt == plaintexts[7 + i]:
                break
            if k == keys[-1]:
                # no matching key found
                raise Exception("Decryption of a ciphertext3 failed!")



    

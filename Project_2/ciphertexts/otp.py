import secrets
import hashlib
import random
import sys
import os

def generate_hash_keys(number_of_keys):
    keys = []

    for _ in range(number_of_keys):
        key1 = secrets.token_bytes(2)
        key1int = int.from_bytes(key1, "big")

        key2shift = ((key1int >> 1) | (key1int >> 15)) & 0xFFFF

        combined_key = key1int.to_bytes(2, "big") + key2shift.to_bytes(2, "big")
        keys.append(hashlib.sha512(combined_key).hexdigest())
    
    return keys

def OTP(hashkeys, messages):
    return ["".join(chr(ord(x) ^ ord(y)) for x, y in zip(message, key)) 
                                         for message, key in zip(messages, hashkeys)]

def read_from_file(path_to_file_directory, number_of_keys, prefix):
    messages = []

    for i in range(number_of_keys):
        filepath = os.path.join(path_to_file_directory, f"{prefix}-{i+1}.txt")
        with open(filepath, "r") as f:
            msg = f.read()
            messages.append(msg)

    return messages

def write_to_file(path_to_file_directory, messages, prefix):
    for i in range(len(messages)):
        filepath = os.path.join(path_to_file_directory, f"{prefix}-{i+1}.txt")
        with open(filepath, "w") as f:
            f.write(messages[i])

def shuffle(messages, keys):
    pairs = list(zip(messages, keys))
    random.shuffle(pairs)
    return pairs

def encrypt(path_to_file_directory, number_of_keys):
    hashkeys = generate_hash_keys(number_of_keys)
    plaintext_messages = read_from_file(path_to_file_directory, number_of_keys, "Plaintext")

    encrypted_messages = OTP(hashkeys[:number_of_keys-3], plaintext_messages[:number_of_keys-3])
    # unique reencrypt
    encrypted_messages.extend(OTP(hashkeys[number_of_keys-3:], plaintext_messages[:3]))
    # reuse reencrypt
    encrypted_messages.extend(OTP(hashkeys[:3], plaintext_messages[number_of_keys-3:]))
    hashkeys.extend(hashkeys[:3])

    encrypted_messages, hashkeys = zip(*shuffle(encrypted_messages, hashkeys))

    write_to_file(path_to_file_directory, encrypted_messages, "Ciphertext")
    write_to_file(path_to_file_directory, hashkeys, "Key")

def decrypt(path_to_file_directory, number_of_keys):
    hashkeys = read_from_file(path_to_file_directory, number_of_keys + 3, "Key")
    encrypted_messages = read_from_file(path_to_file_directory, number_of_keys + 3, "Ciphertext")

    decrypted_messages = OTP(hashkeys, encrypted_messages)

    write_to_file(path_to_file_directory, decrypted_messages, "Decrypted")


if __name__ == "__main__":
    try:
        operation_mode = sys.argv[1]
        path_to_file_directory = sys.argv[2]
        number_of_keys = 10

        if operation_mode == "encrypt":
            encrypt(path_to_file_directory, number_of_keys)
        elif operation_mode == "decrypt":
            decrypt(path_to_file_directory, number_of_keys)
        else:
            raise SystemExit(f"{operation_mode} is not supported. Use encrypt or decrypt")
    except IndexError:
        raise SystemExit(f"Usage: {sys.argv[0]} <encrypt|decrypt> <path_to_file_directory>")

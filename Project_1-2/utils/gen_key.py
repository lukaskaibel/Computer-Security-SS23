import hashlib

def gen_key_from_seed(seed: int ):
    key1int = seed
    key2shift = ((key1int >> 1) | (key1int >> 15)) & 0xFFFF

    combined_key = key1int.to_bytes(2, "big") + key2shift.to_bytes(2, "big")
    return hashlib.sha512(combined_key).hexdigest()

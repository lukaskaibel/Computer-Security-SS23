from utils.file_utils import read_all_files_in_directory
from utils.one_time_pad import otp_decode, generate_final_key
from utils.english_detection import contains_english


ciphertexts = read_all_files_in_directory("ciphertexts", ".txt")
ciphertexts_decoded = []
for ciphertext in ciphertexts:
    ciphertext_decoded = ""
    while not contains_english(ciphertext_decoded):
        key = generate_final_key()
        ciphertext_decoded = otp_decode(ciphertext, key)
    ciphertexts_decoded.append(ciphertext_decoded)
    break

print(ciphertexts_decoded)

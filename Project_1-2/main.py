from utils.one_time_pad import otp_decode, generate_final_key
from utils.english_detection import contains_english
from utils.gen_key import gen_key_from_seed
from ciphertexts.otp import OTP, read_from_file, write_to_file


ciphertexts = read_from_file("./ciphertexts", 13, "Ciphertext")
print(ciphertexts)
ciphertexts_decoded = []
for ciphertext in ciphertexts:
    print("Trying to decode {c}.".format(c=ciphertext))
    ciphertext_decoded = ""
    i = 0
    while not contains_english(ciphertext_decoded):
        if i % 100 == 0:
            print("Reached attempt {i}".format(i=i))
        key = gen_key_from_seed(i)
        ciphertext_decoded = OTP([key], [ciphertext])[0]
        i += 1
    print("[{i}] Decrypted Ciphertext: {cd}".format(i=i, cd=ciphertext_decoded))
    ciphertext_index = ciphertexts.index(ciphertext)
    write_to_file("", [ciphertext_decoded], "Decrypt-Ciphertext-{i}".format(i=ciphertext_index+1))
    write_to_file("", [key], "key-{i}".format(i=ciphertext_index+1))

    ## Check if the key was also used for another ciphertext
    for ciphertext2 in ciphertexts[ciphertext_index+1:]:
        ciphertext_index_2 = ciphertexts.index(ciphertext2)
        ciphertext_decoded2 = OTP([key], [ciphertext2])[0]
        if contains_english(ciphertext_decoded2):
            print("Decrypted also Ciphertext {i} with same key: {cd}".format(i=ciphertext_index_2+1, cd=ciphertext_decoded2))
            write_to_file("", [ciphertext_decoded2], "Decrypt-Ciphertext-{i}".format(i=ciphertext_index_2+1))
            ciphertexts.remove(ciphertext2)


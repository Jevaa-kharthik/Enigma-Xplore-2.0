# import os
# from Crypto.Cipher import AES
# from Crypto.Protocol.KDF import PBKDF2
#
# def multiply_bytes(a, b):
#     return bytes([x ^ y for x, y in zip(a, b)])
# def aes_permutation_decrypt(data, key):
#     # Ensure data is padded to be a multiple of 16 bytes for decryption
#     cipher = AES.new(key, AES.MODE_ECB)
#     decrypted_data = cipher.decrypt(data)
#     return unpad(decrypted_data, 16)  # Remove padding after decryption
#
# def encrypt_keys(password, text, length=16):
#     return PBKDF2(password, text, dkLen=length, count=1000000)
#
# def decrypt(ciphertext, password, termination_vector, important):
#     k1 = encrypt_keys(password, important, 16)
#     k2 = encrypt_keys(password, important[::-1], 16)
#     intermediate = ciphertext
#
#     # Reverse the process (this needs to be careful to match the order and operations in the original encrypt function)
#     for _ in range(num_rounds):
#         intermediate = multiply_bytes(intermediate, k1)
#         intermediate = aes_permutation(intermediate, termination_vector)
#         intermediate = multiply_bytes(intermediate, k2)
#         intermediate = aes_permutation(intermediate, termination_vector)
#
#     # The final step would give you the decrypted result you want
#     return intermediate
#
# # Use the ciphertext you obtained
# decrypted_flag = decrypt(ciphertext, k1, termination_vector, important)
# print("Decrypted Flag:", decrypted_flag)

import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

def multiply_bytes(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

def aes_permutation(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(data, 16))  # Ensure the data is padded

def aes_permutation_decrypt(data, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_data = cipher.decrypt(data)
    return unpad(decrypted_data, 16)  # Remove padding after decryption

def encrypt_keys(password, text, length=16):
    return PBKDF2(password, text, dkLen=length, count=1000000)

def decrypt(ciphertext, password, num_rounds=5):
    termination_vector = ciphertext[:16]
    important = ciphertext[16:32]
    intermediate = ciphertext[32:]

    # Derive the keys using the password and important bytes
    k1 = encrypt_keys(password, important, 16)
    k2 = encrypt_keys(password, important[::-1], 16)

    # Reverse the operations to find the original intermediate
    for _ in range(num_rounds):
        intermediate = multiply_bytes(intermediate, k1)
        intermediate = aes_permutation_decrypt(intermediate, termination_vector)
        intermediate = multiply_bytes(intermediate, k2)
        intermediate = aes_permutation_decrypt(intermediate, termination_vector)

    return intermediate

# Replace 'REDACTED' with the actual value of k1 (password) when you have it
k1 = 'REDACTED'
ciphertext = b'\xe6\x06\x1dh\x03\x19\xd4\xa7\xd5\x9c\xf7e\xa2\xe5\x11\xdaC\xef$U-t\x03lj\xdc\xfd\xb1M<:\x12\x88\xdbg\xec\r\x05I\xd7?\x0eAM1\x83B\x07'
decrypted_data = decrypt(ciphertext, k1, num_rounds=5)  # Ensure num_rounds matches
print("Decrypted Data:", decrypted_data)

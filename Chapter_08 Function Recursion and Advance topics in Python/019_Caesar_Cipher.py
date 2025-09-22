# Caesar Cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is 'shifted' a certain number of places down or up the alphabet.


# Encrypt the message



import string

def encrypt(s, shift):
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    encrypt_msg = ''

    for char in s:
        if char in lower_case:
            encrypt_msg += lower_case[(lower_case.index(char) + shift) % 26]
        elif char in upper_case:
            encrypt_msg += upper_case[(upper_case.index(char) + shift) % 26]
        else:
            encrypt_msg += char

    return encrypt_msg

# Example usage
print(encrypt("Hello, King Caesar!!!", 3))



'''
This Python code defines a function encrypt that performs a Caesar Cipher encryption on a given string s with a specified shift value. The function first creates lists of lowercase and uppercase alphabet letters. It then initializes an empty string encrypt_msg to store the encrypted message. As it iterates through each character in the input string, it checks if the character is a lowercase or uppercase letter. If so, it shifts the character by the specified shift value within the bounds of the alphabet and appends the shifted character to encrypt_msg. If the character is not a letter, it appends the character as is. Finally, it returns the encrypted message. The example given shifts each letter in "Hello, King Caesar!!!" by 3 positions, resulting in "Khoor, Nlqj Fdhvdu!!!".
'''



# Decrypt the messag

import string

def decrypt(s, shift):
    lower_case = list(string.ascii_lowercase)
    upper_case = list(string.ascii_uppercase)
    decrypt_msg = ''

    for char in s:
        if char in lower_case:
            decrypt_msg += lower_case[(lower_case.index(char) - shift) % 26]
        elif char in upper_case:
            decrypt_msg += upper_case[(upper_case.index(char) - shift) % 26]
        else:
            decrypt_msg += char  # Keep non-alphabet characters unchanged

    return decrypt_msg

# Example usage
encrypted_text = "Khoor, Nlqj Fdhvdu!!!"
print(decrypt(encrypted_text, 3))



'''
This Python code defines a function decrypt that performs a Caesar Cipher decryption on a given string s with a specified shift value. The function creates lists of lowercase and uppercase alphabet letters and initializes an empty string decrypt_msg to store the decrypted message. As it iterates through each character in the input string, it checks if the character is a lowercase or uppercase letter. If so, it shifts the character backwards by the specified shift value within the bounds of the alphabet and appends the shifted character to decrypt_msg. If the character is not a letter, it appends the character as is. Finally, it returns the decrypted message. The example given shifts each letter in "Khoor, Nlqj Fdhvdu!!!!!!" backwards by 3 positions, resulting in "Hello, King Caesar!!!!!!".
'''
import string

ALPHABET = string.ascii_lowercase

def caesar(plaintext, shift):
    shifted_alphabet = ALPHABET[shift:] + ALPHABET[:shift]
    table = str.maketrans(ALPHABET, shifted_alphabet)
    return plaintext.translate(table)

if __name__ == "__main__":
    print('Let\'s going to test it')
    print('Ciphering "testing sentence" with 4 moves in Caesar codification')
    cipher_text = caesar('testing sentence', 4)
    print(f"The cipher test is {cipher_text}")
    decipher_text = caesar(f'{cipher_text}', -4)
    print(f"The decode sentence is {decipher_text}")

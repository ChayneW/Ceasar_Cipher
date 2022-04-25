
import art
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#encode = -
#decode = + 

def encode(code, shift):

    new_word = []
    for letter in code:
        if letter in alphabet:
            pos = alphabet.index(letter)
            print(pos)
            new_pos = pos + shift
            new_word.append((alphabet[new_pos]))
        else:
            new_word.append(letter)

    encrypt_word = new_word
    print(f"Cipher: {encrypt_word}")
    return encrypt_word


def decode(code, shift):

    new_word = []
    for letter in code:
        if letter in alphabet:
            pos = alphabet.index(letter)
            print(pos)
            new_pos = pos - shift
            new_word.append((alphabet[new_pos]))
        else:
            new_word.append(letter)

    decrypt_word = new_word
    print(f"Cipher: {decrypt_word}")
    return decrypt_word


is_on = True

while is_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or 'exit':\n")
    
    if direction == 'exit':
        is_on = False
        break

    else:
        text = input("Type your message:\n").lower()
        shift_number = int(input("What's the shift number:\n"))
        shift_number = shift_number % 26

        # if text.isalpha():
        if direction == 'encode':
            encrypted_word = encode(text, shift_number)
            encrypted_word = ''.join(encrypted_word)
            print(f" Text: {text} has been encrypted to: {encrypted_word}\n")
            
        
        elif direction == 'decode':
            decrypted_word = decode(text, shift_number)
            decrypted_word = ''.join(decrypted_word)
            print(f" Text: {text} has been decrypted to: {decrypted_word}\n")              

    # else:
    #     print("Please Input only valid letters.")
    #     pass
        

        




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
len_alphabet = len(alphabet)

"""
def encrypt(text, shift):
  cipher = ""
  for letter in text:
    index = alphabet.index(letter)
    new_index = index + shift
    if new_index >= len_alphabet:
      new_index -= len_alphabet
    cipher += alphabet[new_index]
  print(cipher)

def decrypt(text, shift):
    message = ""
    for letter in text:
        index = alphabet.index(letter)
        new_index = index - shift
        if new_index < 0:
            new_index += len_alphabet
        message += alphabet[new_index]
    print(message)

if direction.lower() == 'encode':
    encrypt(text, shift)
elif direction.lower() == 'decode':
    decrypt(text, shift)
"""
def caesar(text, shift, direction):
    cipher = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        index = alphabet.index(letter)
        new_index = index + shift
        if new_index < 0:
           new_index += alphabet
        elif new_index >= 26:
           new_index -= alphabet
        cipher += alphabet[new_index]
    print(cipher)

caesar(text, shift, direction)
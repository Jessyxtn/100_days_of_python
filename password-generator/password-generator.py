#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_len = len(letters)
symbols_len = len(symbols)
numbers_len = len(numbers)

password = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for letter in range(0, nr_letters):
    seed = random.choice(letters)
    password += letters[seed]

for symbol in range(0, nr_symbols):
    seed = random.randint(0, symbols_len - 1)
    password += symbols[seed]

for number in range(0, nr_numbers):
    seed = random.randint(0, numbers_len - 1)
    password += numbers[seed]

l = list(password)
shuffle = random.shuffle(l)
shuffle_pw = ''.join(l)

print(shuffle_pw)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


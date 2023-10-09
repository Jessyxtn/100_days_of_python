import random
from art import logo

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 5
    if difficulty == 'easy':
        attempts = 10    
    return attempts

def check_num(guess, random_num):
    if guess == random_num:
        print(f"The number is {random_num}. You've guess the correct number!!")
        return True
    elif guess < random_num:
        print("Too low")
    elif guess > random_num:
        print("Too high")
    return False

def game():
    print(logo)
    random_num = random.randint(1, 100)
    print("Welcome to a number guessing game!\nI'm thinking of a number between 1 and 100")

    i = set_difficulty()
    correct = False
    while i != 0 and correct != True:
        print(f"You have {i} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        correct = check_num(guess, random_num)
        i -= 1
        if i == 0:
            print("Sorry, you've ran out of attempts.")

 
if __name__ == "__main__":
    game()
    
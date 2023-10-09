import art
import game_data
import random
import os

def print_celeb(celeb, a_or_b):
    print(f"Compare {a_or_b}: {celeb['name']}, {celeb['description']}, from {celeb['country']}.")

def clear():
    os.system('cls')


if __name__=="__main__":
    score = 0
    lose = False
    while not lose:
        print(art.logo)
        if score != 0:
            print(f"You're right! Current score: {score}.")

        celeb_a =  random.choice(game_data.data)
        a_followers = celeb_a['follower_count']
        print_celeb(celeb_a, 'A')

        print(art.vs)

        celeb_b =  random.choice(game_data.data)
        print_celeb(celeb_b, 'B')
        b_followers = celeb_b['follower_count']

        answer = input("Who has more followers? Type 'A' or 'B': ")

        if (answer == 'A') and (a_followers > b_followers):
            score += 1
            clear()
        elif (answer == 'B') and (b_followers > a_followers):
            score += 1
            os.system('cls')
            clear()
        else:
            os.system('cls')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            lose = True



        

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def win():
    print("congrats you win!")

def lose():
    print("Sorry, I win")

def tie():
    print("It's a tie.")

#Write your code below this line 👇

if __name__ == '__main__':
    player_move = input('Your move, please type "rock", "paper" or "scissors".\n').lower()
    move_list = [rock, paper, scissors]
    pc_move = random.randint(0,2)
    print(f"I play\n {move_list[pc_move]}")

    if pc_move == 0:
        if player_move == 'rock':
            tie()
        elif player_move == 'paper':
            win()
        else:
            lose()
    elif pc_move == 1:
        if player_move == 'rock':
            lose()
        elif player_move == 'paper':
            tie()
        else:
            win()
    elif pc_move == 2:
        if player_move == 'rock':
            win()
        elif player_move == 'paper':
            lose()
        else:
            tie()


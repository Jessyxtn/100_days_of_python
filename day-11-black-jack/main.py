from art import logo
import random
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'K', 'Q', 'A']
picture_cards = ['J', 'Q', 'K', 'A']

def deal():
    two_cards = []
    two_cards.append(random.choice(deck))
    two_cards.append(random.choice(deck))
    return two_cards

def sum_cards(cards):
    result = 0
    for card in cards:
        if card in picture_cards:
            result += 10
        else:
            result += card

    if there_is_ace(cards) and result < 22:
        result += 1
    elif there_is_ace(cards) and result > 21:
        result -= 9

    return result

def there_is_ace(cards):
    if 'A' in cards:
        return True
    else:
        return False

def check_score(player_score, dealer_score):
    if player_score > dealer_score and player_score < 22:
        return True
    elif player_score < 22 and dealer_score > 21:
        return True
    else:
        return False

def hit(cards):
    cards.append(random.choice(deck))

if __name__ == "__main__":

    game_active = True
    while game_active:
        start = input("Would you like to play a game of blackjack? Type 'y' or 'n': ")
        if start == 'y':
            player_cards = deal()
            dealer_cards = deal()
            player_score = sum_cards(player_cards)
            dealer_score = sum_cards(dealer_cards)

            while dealer_score < 17:
                hit(dealer_cards)
                dealer_score = sum_cards(dealer_cards)

            print(f"Your cards: [{player_cards[0]}, {player_cards[1]}], current score: {player_score}")
            print(f"Dealer's first card: {dealer_cards[0]}")

            player_move = 'y'
            while player_score < 22 and player_move != 'n':
                player_move = input("Would you like another card?: ")
                if player_move == 'y':
                    hit(player_cards)
                    player_score = sum_cards(player_cards)
                    print(f"Your new card is {player_cards[-1]}, current score: {player_score}")

            player_win = check_score(player_score, dealer_score)
            
            print(f"Dealer's cards: {dealer_cards}, dealer score: {dealer_score}")
            if (player_score == dealer_score) or (player_score > 22 and dealer_score) > 22:
                print("It's a Tie")
            elif player_win:
                print("Player win")
            else:
                print("Player lose")

        elif start == 'n':
            game_active = False




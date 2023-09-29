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

    if there_is_ace(cards) and result < 21:
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
    pass

def hit(cards):
    cards.append(random.choice(deck))

if __name__ == "__main__":
    start = input("Would you like to play a game of blackjack? Type 'y' or 'n': ")
    if start != 'y':
        exit()
    
    player_cards = deal()
    dealer_cards = deal()
    player_score = sum_cards(player_cards)
    dealer_score = sum_cards(dealer_cards)
    if dealer_score < 17:
        hit(dealer_cards)

    print(f"Your cards: [{player_cards[0]}, {player_cards[1]}], current score: {player_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    check_score()

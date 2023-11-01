import random

def roll_dice():
    return random.randint(1, 6)

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def draw_card():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suit = random.choice(suits)
    rank = random.choice(ranks)
    return f'{rank} of {suit}'

# tests
print(roll_dice())  # output is a random integer between 1 and 6
print(flip_coin())  # output is either 'Heads' or 'Tails'
print(draw_card())  # output is a random card

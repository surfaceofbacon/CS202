import random
suits = ['hearts', 'diamonds', 'clubs',  'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = []
for suit in suits:
        for rank in ranks:
            deck.append(tuple([rank, suit]))
random.shuffle(deck)
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]
print("Player's hand: ", player_hand)
print("Dealer's hand: ", [dealer_hand[1]])


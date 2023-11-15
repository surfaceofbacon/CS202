import random
bankroll = int(input('Please enter your bankroll: '))
suits = ['hearts', 'diamonds', 'clubs',  'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
bad_ranks = ['J', 'Q', 'K', 'A']


def shuffle_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(tuple([rank, suit]))
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand, deck


play = True
wins = 0
losses = 0
def split():
    global hand
    if hand[0] == hand[1]:
        hand1 = [player_hand[0]]
        hand2 = [player_hand[1]]
        hand1.append(deck.pop())
        hand2.append(deck.pop())

def calculate_hand(hand):
    global have_ace
    total = 0
    for card in hand:
        rank = card[0]
        if rank not in bad_ranks:
            total += int(rank)
        else:
            if rank != 'A':
                total += 10
            else:
                have_ace = True
                total += 11
    return int(total)


stand = False

work = True
def play(hand):
    global work
    global bankroll
    global wins
    global losses
    while play:
        bet = int(input('What would you like to bet?: '))
        if bankroll <= 0:
            print('bankroll balance is zero')
            work = False
        else:
            work = True
        if bet > bankroll:
            print('that bet doesnt work')
            work = False
        else:
            work = True
        have_ace = False
        dwon = False
        pwon = False
        if split == 'n':
            hand, dealer_hand, deck = shuffle_deck()
        elif split == 'y':
            dealer_hand, deck = shuffle_deck()
        if work:
            print(f'Your Hand: {hand[0]}, {hand[1]}')
            print(f'Dealers Hand: {dealer_hand[0]}, (??)')
        double_down = input('Would you like to double down (y/n): ')
        if double_down.lower() == 'y':
            hand.append(deck.pop())
            bet *= 2
            print(hand)
        while True and work:
            handval = calculate_hand(hand)
            if handval == 21:
                print('You hit 21!')
                pwon = True
                break
            elif handval > 21:
                if have_ace:
                    handval -= 10
                else:
                    print('You have busted!')
                    dwon = True
                    break
            hit_stay = input('Would you like to hit or stay? h/s: ')
            if hit_stay.lower() == 'h':
                hand.append(deck.pop())
                if handval < 21:
                    print(hand)
                elif handval == 21:
                    print('You hit 21!')
                    pwon = True
                    break
                else:
                    if have_ace:
                        handval -= 10
                    else:
                        print(hand)
                        print('You have busted!')
                        dwon = True
                        break
            elif hit_stay.lower() == 's':
                break
        while True and work:
            stand = False
            counter = 0
            print(counter)
            have_ace = False
            dhandval = calculate_hand(dealer_hand)
            if dwon or pwon:
                break
            if dhandval > 17:
                stand = True
            if dhandval == 21:
                print(f'dealer hand: {dealer_hand}')
                print('The Dealer hit 21, you lost')
                dwon = True
                break
            if dhandval > 21:
                if have_ace:
                    dhandval -= 10
                else:
                    print(f'dealer hand: {dealer_hand}')
                    print('the dealer busted, you win')
                    pwon = True
                    break
            if dhandval > handval:
                print(f'dealer hand: {dealer_hand}')
                print('the dealer wins')
                dwon = True
                break
            if not stand:
                dealer_hand.append(deck.pop())
            counter += 1
        if dwon:
            bankroll -= bet
            losses += 1
        elif pwon:
            bankroll += bet*2
            wins += 1
        print(f'your current bank balance is {bankroll}')
        again = input('would you like to play again? y/n: ')
        if again.lower() == 'n':
            play = False
            print(f'Thanks for playing! You had {wins} wins and {losses} losses')

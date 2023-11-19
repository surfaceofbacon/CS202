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
    #player_hand = [('2', 'diamonds'), ('2', 'clubs')]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand, deck


play = True
wins = 0
losses = 0
def split(hand):
    hand1 = [hand[0]]
    hand2 = [hand[1]]
    hand1.append(deck.pop())
    hand2.append(deck.pop())
    return hand1, hand2

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

def play_hand(hand):
    global have_ace, wins, losses, bankroll, dwon, pwon, dealer_hand, bet, work, handval
    double_down = 'False'

    pwon = False
    handval = calculate_hand(hand)
    #print(hand)
    if handval == 21:
        print('You hit 21!')
        pwon = True
    if not(pwon):
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
    play_dealer()


def play_dealer():
    global have_ace, wins, losses, bankroll, dwon, pwon, dealer_hand, splitted, bet, work, handval
    play1 = True
    stand = False
    have_ace = False
    counter = 0
    while play1 and counter < 10:
        print(dealer_hand)
        print(stand)
        print(have_ace)
        print(dwon)
        print(pwon)
        dhandval = calculate_hand(dealer_hand)
        print(dhandval)
        if dwon:
            print('dealer wins')
            play1 = False
            break
        if pwon:
            print('you win')
        if dhandval > 17:
            stand = True
        if dhandval == 21:
            print(f'dealer hand: {dealer_hand}')
            print('The Dealer hit 21, you lost')
            dwon = True
            play1 = False
            break
        if dhandval > 21:
            if have_ace:
                dhandval -= 10
            else:
                print(f'dealer hand: {dealer_hand}')
                print('the dealer busted, you win')
                pwon = True
                play1 = False
                break
        if stand:
            if dhandval < handval:
                print(f'dealer hand: {dealer_hand}')
                print('your hand beats the dealer hand')
                play1 = False
                pwon = True
                break
            else:
                print(f'dealer hand: {dealer_hand}')
                print('dealer wins')
                play1 = False
                dwon = True
                break
        if not stand:
            dealer_hand.append(deck.pop())
        counter += 1
    if dwon:
        bankroll -= bet
        losses += 1
    elif pwon:
        bankroll += bet * 2
        wins += 1



stand = False


def endgame():
    global play
    play = False
    print(f'Thanks for playing! You had {wins} wins and {losses} losses')



work = True

while play:
    user_split = None
    if bankroll <= 0:
        print('You dont have the funds to play again')
        endgame()
        break
    able_split = False
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
    hand, dealer_hand, deck = shuffle_deck()
    if work:
        print(f'Your Hand: {hand[0]}, {hand[1]}')
        print(f'Dealers Hand: {dealer_hand[0]}, (??)')
    play_hand(hand)
    again = input('would you like to play again? y/n: ')
    if again.lower() == 'n':
        endgame()
    print(f'your current bank balance is {bankroll}')

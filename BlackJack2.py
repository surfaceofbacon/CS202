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
    global have_ace, wins, losses, bankroll, dwon, pwon, dealer_hand, splitted, play, bet, work, handval, dwon1, dwon2
    pwon = False
    if splitted:
        global hand2
    handval = calculate_hand(hand)
    print(hand)
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
            if splitted:
                splitted = False
                play_hand(hand2)
            break
    play_dealer()
def play_dealer():
    global have_ace, wins, losses, bankroll, dwon, pwon, dealer_hand, splitted, play, bet, work, handval, hand1, hand2
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
        if splitted:
            hand1val = calculate_hand(hand1)
            hand2val = calculate_hand(hand2)
            if dhandval > hand1val:
                print(f'dealer hand: {dealer_hand}')
                print('the dealer beats hand 1')
                dwon1 = True
            if dhandval > hand2val:
                print(f'dealer hand: {dealer_hand}')
                print('the dealer beats hand 2')
                dwon2 = True
            if dwon1 or dwon2:
                break
        else:
            if dhandval > handval:
                print(f'dealer hand: {dealer_hand}')
                print('the dealer wins')
                dwon = True

        if not stand:
            dealer_hand.append(deck.pop())
        counter += 1
    if dwon or dwon1 or dwon2:
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
    if bankroll <= 0:
        print('You dont have the funds to play again')
        endgame()
        break
    splitted = False
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
    dwon1 = False
    dwon2 = False
    pwon = False
    hand, dealer_hand, deck = shuffle_deck()
    if work:
        print(f'Your Hand: {hand[0]}, {hand[1]}')
        print(f'Dealers Hand: {dealer_hand[0]}, (??)')
    if hand[0][0] == hand[1][0]:
        able_split = True
        user_split = input('Would you like to split? y/n: ')
    if able_split and user_split.lower() == 'y':
        splitted = True
        hand1, hand2 = split(hand)
        play_hand(hand1)
    else:
        play_hand(hand)
    again = input('would you like to play again? y/n: ')
    if again.lower() == 'n':
        endgame()
    print(f'your current bank balance is {bankroll}')

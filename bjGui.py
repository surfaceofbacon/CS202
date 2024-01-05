"""
Final Project

Python GUI Blackjack Game

This is a graphical user interface (GUI) implementation of the classic card game Blackjack, written in Python using the Tkinter library.
It includes basic game play as well as double down and split features using object-oriented programming (OOP) principles. The game uses
card images provided in the "Images" folder.

Created by Thomas Nelson and Russell Christensen for computer science 202, Truckee Meadows Community College
Date: 11/15/23

"""

import tkinter as tk
from tkinter import messagebox
import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()

    def _get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)

class Deck:
    def __init__(self):
        self.cards = [Card(s, r) for s in ["S", "C", "H", "D"] for r in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]]
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.aces += 1
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = Hand()

    def hit(self, deck):
        self.hand.add_card(deck.draw_card())

    def double_down(self, deck):
        self.hit(deck)
        self.stand()

    def split(self, deck):
        if Hand.cards[0][0] == Hand.cards[1][0]:
            pass

    def stand(self):
        Blackjack.calculate_score(Hand.cards)

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player('Player')
        self.dealer = Player('Dealer')
        self.dealer2 = Player('Dealer2')
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hit(self.deck)
        self.dealer2.hit(self.deck)
        self.dealer2.hit(self.deck)

        self.player2 = Player('Player2')
        self.player2.hit(self.deck)
        self.player2.hit(self.deck)

    def calculate_score(self, cards):
        card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        num_aces = 0
        total_score = 0
        
        for card in cards:
            card_value = card[0]
            if card_value == 'A':
                num_aces += 1
            total_score += card_values[card_value]

        while total_score > 21 and num_aces > 0:
            total_score -= 10
            num_aces -= 1

        return total_score

    def push(self):
        if Blackjack.calculate_score(self.player) == Blackjack.calculate_score(self.dealer):
            pass

    def play_hand(self):
        pass

class BlackjackGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Blackjack')
        self.geometry('800x600')
        self.resizable(False, False)

        self.canvas = tk.Canvas(self, width = 800, height = 600)
        self.canvas.pack()

        self.menu = tk.Menu(self)
        self.config(menu=self.menu)

        self.game_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label = 'Game', menu = self.game_menu)
        self.game_menu.add_command(label='New Game', command=self.start_game)
        self.game_menu.add_command(label='Exit', command=self.quit)

        self.help_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=self.help_menu)
        self.help_menu.add_command(label='Rules', command=self.show_rules)
        self.help_menu.add_command(label='About', command=self.show_about)

        self.start_button = tk.Button(self, text='Start Game', command=self.start_game)
        self.canvas.create_window(400, 300, window=self.start_button)
        self.directory = 'C:\\Users\\rcind\OneDrive\Documents\GitHub\CS202\card1\\'

        self.bankroll_label = tk.Label(self, text = 'Enter a bankroll (1-5000):')
        self.canvas.create_window(330, 200, window = self.bankroll_label)
        
        vcmd = self.register(self.validate_bankroll)
        self.bankroll_entry = tk.Entry(self, validate = 'key', validatecommand = (vcmd, '%P'))
        self.canvas.create_window(340, 230, window = self.bankroll_entry)
        self.bet_value = 5
        self.win = 0
        self.loss = 0
        self.bankroll_amount = 0
        self.count = 0
        self.hit_count = 0

        self.mainloop()
    

    def start_game(self):
        self.blackjack = Blackjack()
        if self.count == 0:
            self.bankroll_amount = int(self.bankroll_entry.get())
            self.count += 1
        self.canvas.delete('all')
        self.canvas.create_text(400, 50, text=f"{self.blackjack.player.name}'s Hand", font=('Arial', 16))
        self.canvas.create_text(400, 350, text=f"{self.blackjack.dealer.name}'s Hand", font=('Arial', 16))

        self.player_hand_images = []
        self.player_hand_value = self.blackjack.player.hand.value
        for i, card in enumerate(self.blackjack.player.hand.cards):
            img = tk.PhotoImage(file = f"{self.directory}{card.suit}{card.rank}.png").subsample(2,2)
            self.player_hand_images.append(img)
            self.canvas.create_image(100 + i * 70, 200, image = img)

        self.dealer_hand_images = []
        self.dealer_hand_value = self.blackjack.dealer.hand.value
        for i, card in enumerate(self.blackjack.dealer.hand.cards):
            img = tk.PhotoImage(file = f"{self.directory}{card.suit}{card.rank}.png").subsample(3, 3)
            img1 = tk.PhotoImage(file = f"{self.directory}card_back.png").subsample(3, 3)
            self.dealer_hand_images.append(img)
            self.dealer_hand_images.append(img1)
            if i == 0:
                self.canvas.create_image(100 + i * 70, 450, image = img1)
            else:
                self.canvas.create_image(100 + i * 70, 450, image = img)

        revealed_card = self.blackjack.dealer.hand.cards[1]
        revealed_card_value = revealed_card.value

        self.player_value_text = self.canvas.create_text(400, 250, text = f"Value: {self.player_hand_value}", font=('Arial', 16))
        self.dealer_value_text = self.canvas.create_text(400, 500, text = f"Value: {revealed_card_value} + ?", font=('Arial', 16))

        self.hit_button = tk.Button(self, text = 'Hit', command = self.hit)
        self.canvas.create_window(200, 550, window=self.hit_button)
        self.stand_button = tk.Button(self, text = 'Stand', command=self.stand)
        self.canvas.create_window(300, 550, window=self.stand_button)
        self.double_down_button = tk.Button(self, text='Double Down', command=self.double_down)
        self.canvas.create_window(400, 550, window=self.double_down_button)
        self.split_button = tk.Button(self, text='Split', command=self.split)
        self.canvas.create_window(500, 550, window=self.split_button)

        self.bet_button = tk.Button(self, text = 'Increase Bet', command = self.increase_bet)
        self.canvas.create_window(100, 550, window = self.bet_button)
        self.deal_button = tk.Button(self, text = 'Deal new hand', command = self.deal_new_hand)
        self.canvas.create_window(600, 550, window = self.deal_button)
        
        self.first_hand = 0
        self.split_count = 0

        self.player_bwl = self.canvas.create_text(300, 575, text = f"Win/loss: {self.win}/{self.loss} Bankroll: {self.bankroll_amount}")

    def hit(self):
        if self.split_count == 1:
            self.hit_count += 1
            self.blackjack.player.hit(self.blackjack.deck)
            self.update_player_hand()
            if self.blackjack.player.hand.value > 21:
                self.loss += 1
                self.bankroll_amount -= self.bet_value
                self.hit_button.destroy()
                self.stand_button.destroy()
                self.split_count += 1
        else:
            self.hit_count += 1
            self.blackjack.player.hit(self.blackjack.deck)
            self.update_player_hand()
            if self.blackjack.player.hand.value > 21:
                self.loss += 1
                self.bankroll_amount -= self.bet_value
                self.deal_new_hand()
        
    def stand(self):
        if self.split_count == 1:
            while self.blackjack.dealer.hand.value < 17:
                self.blackjack.dealer.hit(self.blackjack.deck)
            if self.blackjack.dealer.hand.value == self.blackjack.player.hand.value:
                self.hit_button.destroy()
                self.stand_button.destroy()
                self.split_count += 1
            elif self.blackjack.dealer.hand.value > 21:
                self.win += 1
                self.bankroll_amount += self.bet_value
                self.hit_button.destroy()
                self.stand_button.destroy()
                self.split_count += 1
            elif self.blackjack.player.hand.value > self.blackjack.dealer.hand.value:
                self.win += 1
                self.bankroll_amount += self.bet_value
                self.hit_button.destroy()
                self.stand_button.destroy()
                self.split_count += 1
            else:
                self.loss += 1
                self.bankroll_amount -= self.bet_value
                self.hit_button.destroy()
                self.stand_button.destroy()
                self.split_count += 1
        else:
            while self.blackjack.dealer.hand.value < 17:
                self.blackjack.dealer.hit(self.blackjack.deck)
            self.update_dealer_hand()
            if self.blackjack.dealer.hand.value == self.blackjack.player.hand.value:
                self.deal_new_hand()
            elif self.blackjack.dealer.hand.value > 21:
                self.win += 1
                self.bankroll_amount += self.bet_value
                self.deal_new_hand()
            elif self.blackjack.player.hand.value > self.blackjack.dealer.hand.value:
                self.win += 1
                self.bankroll_amount += self.bet_value
                self.deal_new_hand()
            else:
                self.loss += 1
                self.bankroll_amount -= self.bet_value
                self.deal_new_hand()

    def double_down(self):
        self.hit_count += 1
        self.blackjack.player.hit(self.blackjack.deck)
        self.update_player_hand()
        self.bet_value = self.bet_value * 2
        if self.blackjack.player.hand.value > 21:
            self.loss += 1
            self.bankroll_amount -= self.bet_value
            self.deal_new_hand()

    def split(self):
        player_hand = self.blackjack.player.hand

        # Check if the player has exactly two cards and if they have the same rank
        if len(player_hand.cards) == 2 and player_hand.cards[0].rank == player_hand.cards[1].rank:
            # Create two new hands for the player
            hand1 = Hand()
            hand2 = Hand()
            hand1.add_card(player_hand.cards[0])
            hand2.add_card(player_hand.cards[1])

            # Add a new card to each hand from the deck
            hand1.add_card(self.blackjack.deck.draw_card())
            hand2.add_card(self.blackjack.deck.draw_card())

            # Update player's hand to two separate hands
            self.blackjack.player.hand = hand1
            self.blackjack.player2.hand = hand2

            # Update the GUI to display both hands separately
            self.canvas.delete('all')
            self.canvas.create_text(200, 50, text=f"{self.blackjack.player.name}'s Hand 1", font=('Arial', 16))
            self.canvas.create_text(600, 50, text=f"{self.blackjack.player.name}'s Hand 2", font=('Arial', 16))

            # Display Hand 1
            self.player_hand_images = []
            for i, card in enumerate(self.blackjack.player.hand.cards):
                img = tk.PhotoImage(file=f"{self.directory}{card.suit}{card.rank}.png").subsample(2, 2)
                self.player_hand_images.append(img)
                self.canvas.create_image(100 + i * 70, 200, image=img)
            self.dealer_hand_images = []
            self.dealer_hand_value = self.blackjack.dealer.hand.value
            for i, card in enumerate(self.blackjack.dealer.hand.cards):
                img = tk.PhotoImage(file = f"{self.directory}{card.suit}{card.rank}.png").subsample(3, 3)
                img1 = tk.PhotoImage(file = f"{self.directory}card_back.png").subsample(3, 3)
                self.dealer_hand_images.append(img)
                self.dealer_hand_images.append(img1)
                if i == 0:
                    self.canvas.create_image(100 + i * 70, 450, image = img1)
                else:
                    self.canvas.create_image(100 + i * 70, 450, image = img)

            revealed_card = self.blackjack.dealer.hand.cards[1]  # Get the revealed card
            revealed_card_value = revealed_card.value

            self.player_value_text = self.canvas.create_text(200, 100, text = f"Value: {self.blackjack.player.hand.value}", font=('Arial', 16))
            self.dealer_value_text = self.canvas.create_text(200, 300, text = f"Value: {revealed_card_value} + ?", font=('Arial', 16))

            # Display Hand 2
            self.player_hand_images2 = []
            for i, card in enumerate(hand2.cards):
                img = tk.PhotoImage(file=f"{self.directory}{card.suit}{card.rank}.png").subsample(2, 2)
                self.player_hand_images2.append(img)
                self.canvas.create_image(500 + i * 70, 200, image=img)

            self.dealer_hand_images2 = []
            self.dealer_hand_value = self.blackjack.dealer2.hand.value
            for i, card in enumerate(self.blackjack.dealer2.hand.cards):
                img = tk.PhotoImage(file = f"{self.directory}{card.suit}{card.rank}.png").subsample(3, 3)
                img1 = tk.PhotoImage(file = f"{self.directory}card_back.png").subsample(3, 3)
                self.dealer_hand_images2.append(img)
                self.dealer_hand_images2.append(img1)
                if i == 0:
                    self.canvas.create_image(400 + i * 70, 450, image = img1)
                else:
                    self.canvas.create_image(400 + i * 70, 450, image = img)

            revealed_card2 = self.blackjack.dealer2.hand.cards[1]
            revealed_card_value2 = revealed_card2.value
            self.dealer_value_text = self.canvas.create_text(400, 300, text = f"Value: {revealed_card_value2} + ?", font = ('Arial', 16))

            self.hit_button = tk.Button(self, text = 'Hit', command = self.hit)
            self.canvas.create_window(100, 550, window=self.hit_button)
            self.stand_button = tk.Button(self, text = 'Stand', command=self.stand)
            self.canvas.create_window(150, 550, window=self.stand_button)

            self.hit_button2 = tk.Button(self, text = 'Hit', command = self.hit_split)
            self.canvas.create_window(400, 550, window=self.hit_button2)
            self.stand_button2 = tk.Button(self, text = 'Stand', command=self.stand_split)
            self.canvas.create_window(450, 550, window=self.stand_button2)

            self.player_value_text = self.canvas.create_text(500, 100, text = f"Value: {self.blackjack.player2.hand.value}", font=('Arial', 16))

            self.split_count = 1

    def update_player_hand(self):
        self.canvas.delete(self.player_value_text)
        self.player_hand_value = self.blackjack.player.hand.value
        for i, card in enumerate(self.blackjack.player.hand.cards):
            img = tk.PhotoImage(file = f"{self.directory}{card.suit}{card.rank}.png").subsample(2, 2)
            self.player_hand_images.append(img)
            self.canvas.create_image(100 + i * 70, 200, image = img)
        self.player_value_text = self.canvas.create_text(400, 300, text=f"Value: {self.player_hand_value}", font=('Arial', 16))

    def update_dealer_hand(self):
        self.canvas.delete(self.dealer_value_text)
        self.dealer_hand_value = self.blackjack.dealer.hand.value
        revealed_card = self.blackjack.dealer.hand.cards[0]  # Get the revealed card
        revealed_card_value = revealed_card.value

        for i, card in enumerate(self.blackjack.dealer.hand.cards):
            img = tk.PhotoImage(file = f"{self.directory}{card.suit}{card.rank}.png").subsample(3, 3)
            self.dealer_hand_images.append(img)
            if i == 0:
                self.canvas.create_image(100, 450, image = tk.PhotoImage(file = f'{self.directory}card_back.png'))
            else:
                self.canvas.create_image(100 + i * 70, 450, image = img)
        self.dealer_value_text = self.canvas.create_text(400, 500, text = f"Value: {revealed_card_value} + ?", font=('Arial', 16))

    def validate_bankroll(self, new_value):
        return new_value.isdigit() and 1 <= int(new_value) <= 5000
    
    def increase_bet(self):
        if self.bet_value < self.bankroll_amount and self.hit_count < 1:
            self.bet_value += 5

    def deal_new_hand(self):
        self.first_hand += 1
        self.hit_count = 0
        self.canvas.delete('all')
        self.start_game()

    def hit_split(self):
        if self.split_count == 1:
            self.hit_count += 1
            self.blackjack.player2.hit(self.blackjack.deck)
            self.update_player_hand()
            if self.blackjack.player2.hand.value > 21:
                self.loss += 1
                self.bankroll_amount -= self.bet_value
                self.hit_button2.destroy()
                self.stand_button2.destroy()
                self.split_count += 1
        else:
            self.hit_count += 1
            self.blackjack.player2.hit(self.blackjack.deck)
            self.update_player_hand()
            if self.blackjack.player2.hand.value > 21:
                self.loss += 1
                self.bankroll_amount -= self.bet_value
                self.deal_new_hand()
        
    def stand_split(self):
        if self.split_count == 1:
            while self.blackjack.dealer2.hand.value < 17:
                self.blackjack.dealer2.hit(self.blackjack.deck)
            if self.blackjack.dealer2.hand.value == self.blackjack.player2.hand.value:
                self.hit_button2.destroy()
                self.stand_button2.destroy()
                self.split_count += 1
            elif self.blackjack.dealer2.hand.value > 21:
                self.win += 1
                self.bankroll_amount += self.bet_value
                self.hit_button2.destroy()
                self.stand_button2.destroy()
                self.split_count += 1
            elif self.blackjack.player2.hand.value > self.blackjack.dealer2.hand.value:
                self.win += 1
                self.bankroll_amount += self.bet_value
                self.hit_button2.destroy()
                self.stand_button2.destroy()
                self.split_count += 1
            else:
                self.loss += 1
                self.bankroll_amount -= self.bet_value
                self.hit_button2.destroy()
                self.stand_button2.destroy()
                self.split_count += 1
        else:
            while self.blackjack.dealer2.hand.value < 17:
                self.blackjack.dealer2.hit(self.blackjack.deck)
            self.update_dealer_hand()
            if self.blackjack.dealer2.hand.value == self.blackjack.player2.hand.value:
                self.deal_new_hand()
            elif self.blackjack.dealer2.hand.value > 21:
                self.win += 1
                self.bankroll_amount += self.bet_value
                self.deal_new_hand()
            elif self.blackjack.player2.hand.value > self.blackjack.dealer2.hand.value:
                self.win += 1
                self.bankroll_amount += self.bet_value
                self.deal_new_hand()
            else:
                self.loss += 1
                self.bankroll_amount -= self.bet_value
                self.deal_new_hand()

    def update_player_hand_split(self):
        self.canvas.delete(self.player_value_text)
        self.player_hand_value = self.blackjack.player2.hand.value
        for i, card in enumerate(self.blackjack.player2.hand.cards):
            img = tk.PhotoImage(file = f"{self.directory}{card.suit}{card.rank}.png").subsample(2, 2)
            self.player_hand_images2.append(img)
            self.canvas.create_image(100 + i * 70, 200, image = img)
        self.player_value_text = self.canvas.create_text(400, 100, text=f"Value: {self.blackjack.player2.hand.value}", font=('Arial', 16))

    def show_rules(self):
        messagebox.showinfo('Rules', 'The goal of blackjack is to beat the dealer by having a hand value of 21 or as close to 21 as possible without going over. Face cards are worth 10, Aces are worth 1 or 11, and all other cards are worth their face value.')

    def show_about(self):
        messagebox.showinfo('About', 'This game was created by Thomas Nelson using Python and Tkinter.')

if __name__ == '__main__':
    app = BlackjackGUI()

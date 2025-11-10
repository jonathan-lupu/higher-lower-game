from os import wait3
from traceback import print_tb
from typing import LiteralString

from deck import Deck
from card import Card




class Game:
    def __init__(self):
        self.deck = Deck()
        self.current_card = None
        self.previous_card = None
        self.score = 0

    def start_game(self):
        self.deck.generate_deck()
        self.deck.shuffle()
        self.previous_card = self.deck.draw()


    def handle_guess(self, guess):
        answer = self.compare()

        if answer == "HIGHER" and guess == "h":
            self.score +=1
            return True
        elif answer == "LOWER" and guess == "l":
            self.score +=1
            return True
        else:
            return False

    def compare(self):
        self.current_card = self.deck.draw()
        print(f"comparing {self.current_card} to {self.previous_card}")
        if self.current_card.get_comparison_value() > self.previous_card.get_comparison_value():
            return "HIGHER"
        else:
            return "LOWER"

    def next_round(self):
        self.previous_card = self.current_card
        self.current_card = self.deck.draw()

    def handle_input(self):
        valid_input = False
        while not valid_input:
            guess = input(f"Guess if the next card is higher (H/h) or lower (L/l) "
                          f"than {self.previous_card}: ")
            guess.strip().lower()

            if guess == "h" or guess == "l":
                return guess
            else:
                print("Invalid input. Please try again.\n")

    def game_loop(self):
        self.start_game()
        correct = True
        while correct:
            guess = self.handle_input()
            if self.handle_guess(guess):
                print("...")
                print(f"Correct guess! The card was {self.current_card}")
                self.next_round()
            else:
                correct = False
                print("Sorry, incorrect guess.")
                print(f"the card was {self.previous_card}")










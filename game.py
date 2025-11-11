from enum import Enum
from deck import Deck

class Result(Enum):
    HIGHER = 1
    DRAW = 2
    LOWER = 3


class Game:
    def __init__(self):
        self.deck = Deck()
        self.current_card = None
        self.previous_card = None
        self.score = 0

    def start_game(self):
        self.deck.reset_cards()
        self.deck.generate_deck()
        self.deck.shuffle()
        self.previous_card = self.deck.draw()
        self.current_card = None



    def handle_guess(self, guess):
        answer = self.compare()
        # If cards are equal value - keep playing, no change in score
        if answer == Result.DRAW:
            print("It's a draw! - no change in points")
            return True
        if answer == Result.HIGHER and guess == "h":
            self.score +=1
            print("...")
            print(f"Correct guess! The card was {self.current_card}")
            return True
        elif answer == Result.LOWER and guess == "l":
            self.score +=1
            print("...")
            print(f"Correct guess! The card was {self.current_card}")
            return True
        else:
            return False

    def compare(self):
        self.current_card = self.deck.draw()
        if self.current_card.get_comparison_value() > self.previous_card.get_comparison_value():
            return Result.HIGHER
        elif self.current_card.get_comparison_value() == self.previous_card.get_comparison_value():
            return Result.DRAW
        else:
            return Result.LOWER

    def next_round(self):
        self.previous_card = self.current_card
        self.current_card = self.deck.draw()

    def handle_input(self, action):
        valid_input = False
        while not valid_input:
            if action == "GUESS":
                guess = input(f"Guess if the next card is higher (H/h) or lower (L/l) "
                              f"than {self.previous_card}: ")
                guess = guess.strip().lower()

                if guess == "h" or guess == "l":
                    return guess
                else:
                    print("Invalid input. Please try again.\n")
            elif action == "END":
                action_inp = input("Would you like to play again? (Y/N) ")
                action_inp = action_inp.strip().lower()
                if action_inp == "n":
                    return "END"
                elif action_inp == "y":
                    return "AGAIN"
                else:
                    print("Invalid input. Please try again.\n")

    def game_loop(self):
        self.start_game()
        correct = True
        while correct and not self.deck.is_empty():
            guess = self.handle_input("GUESS")
            # Correct guess / draw
            if self.handle_guess(guess):
                self.next_round()
            else:
                correct = False
                print("Sorry, incorrect guess.")
                print(f"You scored {self.score} points.")
                print(f"The card was {self.current_card}")
                if self.handle_input("END") == "AGAIN":
                    print("Restarting...")
                    self.start_game()
                    correct = True
                else:
                    print("Quitting game")










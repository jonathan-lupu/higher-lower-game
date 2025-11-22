from deck import Deck
from enum import Enum

class Result(Enum):
    """
    Enum representing possible outcomes of a card comparison.

    Used to standardise result values passed between functions for clarity and safety.

    Members:
        HIGHER (int): Indicates the new card is higher in value.
        DRAW (int): Indicates both cards have equal value.
        LOWER (int): Indicates the new card is lower in value.
    """
    HIGHER = 1
    DRAW = 2
    LOWER = 3


class Game:
    def __init__(self):
        self.deck = Deck()
        self.current_card = None
        self.previous_card = None
        self.score = 0
        self.high_score = 0

        try:
            with open("highscore.txt", "r") as highscore_file:
                self.high_score = int(highscore_file.read())
        except FileNotFoundError:
            # handle the missing file - create the file
            with open("highscore.txt", "w") as f:
                pass
            self.high_score = 0

    def start_game(self):
        """
        Sets up the game, called at the start of the game and when restarting
        Resets deck, and configures deck with shuffled cards
        :return: None
        """
        self.deck.reset_cards()
        self.deck.generate_deck()
        self.deck.shuffle()
        self.previous_card = self.deck.draw()
        self.current_card = None
        self.score = 0


    def handle_guess(self, guess):
        """
        Evaluate the player's guess against the actual card comparison result.

        Calls compare() to determine whether the new card is higher, lower, or equal in value.
        Updates the score and prints feedback accordingly.

        :param: guess (str): Player's input, "h" for higher or "l" for lower.

        :return:
            bool: True if the guess is correct or the result is a draw; False otherwise.
        """
        # Answer by comparing the two cards: Higher, Lower, Draw
        answer = self.compare_cards()

        # If cards are equal value - keep playing, no change in score
        if answer == Result.DRAW:
            msg = f"It's a draw! - no change in points"
            return True,msg
        if answer == Result.HIGHER and guess == "higher":
            self.score +=1
            msg = f"Correct guess!"
            return True,msg
        elif answer == Result.LOWER and guess == "lower":
            self.score +=1
            msg = f"Correct guess!"
            return True,msg
        else:
            msg = "Incorrect guess!"
            return False, msg

    def compare_cards(self):
        """
        Compare the current card to the previous card and determine the result.

        Draws a new card from the deck, then compares its value against the previous card's value.

        :return:
            Result: One of Result.HIGHER, Result.DRAW, or Result.LOWER
        """
        self.current_card = self.deck.draw()
        if self.current_card.get_comparison_value() > self.previous_card.get_comparison_value():
            return Result.HIGHER
        elif self.current_card.get_comparison_value() == self.previous_card.get_comparison_value():
            return Result.DRAW
        else:
            return Result.LOWER

    def next_round(self):
        """
        Updates the previous card to the current card and draws a new card from the deck
        to become the new current card.

        :return: None
        """
        self.previous_card = self.current_card
        self.current_card = self.deck.draw()

    def set_high_score(self):
        """
        Updates the high score saved in highscore.txt if the score achieved is higher than saved highscore.
        :return: None
        """
        if self.score > self.high_score:
            self.high_score = self.score
        with open(f"highscore.txt", "w") as highscore_file:
            highscore_file.write(str(self.high_score))

    def handle_input(self, action):
        """
        DEPRECATED function not in use with GUI implementation.
        Prompt and validate user input based on game state.

        For in-game guesses, requests whether the next card is higher or lower
        than the previous card and returns a normalized response.
        At end of game, asks whether the player wants to restart or quit.

        :param:
            action (str): "GUESS" to request higher/lower input,
                          "END" to request restart/quit decision.

        :return:
            str:
                - "h" or "l" for a valid guess input.
                - "AGAIN" if the player chooses to restart.
                - "END" if the player chooses to quit.
        """
        valid_input = False
        inputs = ("h" , "l")
        while not valid_input:
            if action == "GUESS":
                guess = input(f"Guess if the next card is higher (H/h) or lower (L/l) "
                              f"than {self.previous_card}: ")
                guess = guess.strip().lower()

                if guess in inputs:
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
        return None

    def game_loop(self):
        """
        DEPRECATED function not in use with GUI implementation.
        Run the main game loop.

        Continuously prompts the player to guess whether the next card will be higher or lower.
        Ends when the player guesses incorrectly or the deck is exhausted.
        After a loss, prompts the player to restart or quit.

        Calls:
            start_game() – initializes or restarts game state.
            handle_input() – retrieves player input for guesses and restart choice.
            handle_guess() – checks correctness of guess.
            next_round() – advances game state after a correct guess.

        :return:
            None
        """
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
import random
from card import Card
class Deck:

    def __init__(self):
        self.cards = []

    def generate_deck(self, include_joker=False):
        """
            Populate the deck with standard playing cards.

            Creates a full 52-card deck consisting of four suits and thirteen ranks.
            Optionally includes jokers if specified.

            :param:
                include_joker (bool): Whether to include jokers in the deck. Defaults to False.

            :return:
                None
        """
        suits = ['♣', '♦', '♥', '♠']
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        """
        Randomise the order of cards in the deck using the Fisher–Yates shuffle algorithm.

        Iterates backward through the deck, swapping each card with another randomly chosen card
        to ensure an unbiased shuffle.

        :return:
            None
        """
        for i in range(len(self.cards)-1 ,0, -1):
            j = random.randint(0,i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def draw(self):
        """
        Remove and return the top card from the deck.

        :return:
            Card: The card drawn from the top of the deck.
        """
        return self.cards.pop()

    def is_empty(self):
        """
        Check if the deck has any remaining cards.

        :return:
            bool: True if the deck is empty, False otherwise.
        """
        return len(self.cards) == 0

    def reset_cards(self):
        """
        Reset the deck cards to an empty list.
        :return: None
        """
        self.cards = []
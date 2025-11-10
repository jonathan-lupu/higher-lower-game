import random

from card import Card
from random import randint

class Deck:

    def __init__(self):
        self.cards = []

    def generate_deck(self, include_joker=False):
        suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        for i in range(len(self.cards)-1 ,0, -1):
            j = random.randint(0,i + 1)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def draw(self):
        return self.cards.pop()

    def is_empty(self):
        return len(self.cards) == 0

    def reset_cards(self):
        self.cards = []
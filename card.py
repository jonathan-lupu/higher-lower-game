class Card:
    def __init__(self, suit, rank):
        self.value = None
        self.suit = suit
        self.rank = rank
        self.set_value(rank)


    def set_value(self, rank : str):
        """
        Sets internal value to int for comparison
            :param: rank : str - rank of the card e.g. Ace, 1, 3, King
            :return: None - sets attribute
        """
        # Not using match-case due to maximise python version compatability
        if rank == "King":
            self.value = 13
        elif rank == "Queen":
            self.value = 12
        elif rank == "Jack":
            self.value = 11
        elif rank == "Ace":
            self.value = 1
        else:
            self.value = int(rank)

    def __str__(self):
        """
        Returns string representation of card
        :return: str in format of "rank" of "suit" e.g. Ace of Hearts
        """
        return f"{self.rank} {self.suit}"

    def get_comparison_value(self):
        """
        Return the internal value of the card to be used for comparison

        :return: int: internal comparison value
        """
        return self.value




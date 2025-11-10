class Card:
    def __init__(self, suit, rank):
        self.value = None
        self.suit = suit
        self.rank = rank
        self.set_value(rank)


    def set_value(self, rank : str):
        """Sets internal value to int for comparison
            Arguments:
                rank : str - rank of the card e.g. Ace, 1, 3, King
            Returns: None - sets attribute
            """
        match rank:
            case "King":
                self.value = 13
            case "Queen":
                self.value = 12
            case "Jack":
                self.value = 11
            case "Ace":
                self.value = 1
            case _:
                self.value = int(rank)


    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def get_comparison_value(self):
        return self.value




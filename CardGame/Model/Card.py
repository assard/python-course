import dataclasses

RANKS = (
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "valet",
    "queen",
    "king",
    "as",
)

SUITS = ("heart", "shamrock", "spade", "diamond")


class Card:
    def __init__(self, rank: str, suit: str, hidden: bool = True):
        self._rank = rank
        self._suit = suit
        self._hidden = hidden

    def __str__(self):
        return f"{self._rank} of {self._suit}"

    def __repr__(self):
        return str(self)

    def get_rank_score(self):
        return RANKS.index(self._rank)

    def get_suit_score(self):
        return SUITS.index(self._suit)

    def is_rank_high(self, other_card: "Card") -> bool:
        return self.get_rank_score() > other_card.get_rank_score()

    def is_suit_high(self, other_card: "Card") -> bool:
        return self.get_suit_score() > other_card.get_suit_score()

    def show(self):
        self._hidden = False

    def hide(self):
        self._hidden = True

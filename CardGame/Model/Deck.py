import random

from CardGame.Model.Card import RANKS, SUITS, Card


class Deck(list):
    def __init__(self):
        for rank in RANKS:
            for suit in SUITS:
                card = Card(rank, suit)
                self.append(card)
        self.shuffle()

    def shuffle(self):
        random.shuffle(self)

    def draw_card(self):
        return self.pop()

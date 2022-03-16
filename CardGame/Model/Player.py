from CardGame.Model.Card import Card
from CardGame.Model.Hand import Hand


class Player:
    def __init__(self, name: str):
        self._name = name
        self._hand = Hand()

    def take_card(self, card: Card):
        self._hand.append(card)

    def retrieve_card(self):
        return self._hand.pop()

    def __str__(self):
        return self._name

    def get_card(self):
        return self._hand[0]

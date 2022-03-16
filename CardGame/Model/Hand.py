from CardGame.Model.Card import Card


class Hand(list):
    def append(self, object):
        if not isinstance(object, Card):
            raise ValueError(f"You must append an object of type {Card}")
        return super().append(object)

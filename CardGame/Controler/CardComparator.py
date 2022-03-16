from abc import ABC

from usbcreator.backends.base.backend import abstract

from CardGame.Model.Card import Card


class CardComparator(ABC):
    @abstract
    def get_winner_card(self, first_card: Card, second_card: Card) -> Card:
        pass

    def _is_not_rank_equal(self, first_card: "Card", second_card: "Card") -> bool:
        return first_card.get_rank_score() != second_card.get_rank_score()


class CardComparatorHigherWinner(CardComparator):
    def get_winner_card(self, first_card: Card, second_card: Card) -> Card:
        if self._is_not_rank_equal(first_card, second_card):
            if first_card.is_rank_high(second_card):
                return first_card
            return second_card
        if first_card.is_suit_high(second_card):
            return first_card
        return second_card


class CardComparatorLowerWinner(CardComparator):
    def get_winner_card(self, first_card: Card, second_card: Card) -> Card:
        if self._is_not_rank_equal(first_card, second_card):
            if first_card.is_rank_high(second_card):
                return second_card
            return first_card
        if first_card.is_suit_high(second_card):
            return second_card
        return first_card

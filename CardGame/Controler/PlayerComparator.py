from CardGame.Controler.CardComparator import CardComparator
from CardGame.Model.Player import Player


class PlayerComparator:
    def __init__(self, card_comparator: CardComparator):
        self._card_comparator = card_comparator

    def get_winner(self, first_player: Player, second_player: Player) -> Player:
        first_player_card = first_player.get_card()
        second_player_card = second_player.get_card()
        winner_card = self._card_comparator.get_winner_card(
            first_player_card, second_player_card
        )
        if first_player_card == winner_card:
            return first_player
        return second_player

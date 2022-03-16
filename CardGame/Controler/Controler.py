from CardGame.Controler.PlayerComparator import PlayerComparator
from CardGame.Model.Deck import Deck
from CardGame.Model.Player import Player
from CardGame.View.View import View


class Controler:
    def __init__(
        self,
        view: View,
        player_comparator: PlayerComparator,
    ):
        self.player_comparator = player_comparator
        self._view = view

    def launch_game(self):
        self._players = self._initiate_players()
        self._deck = Deck()

    def play_round(self):
        self._deck.shuffle()
        self._distribute_card()
        self._show_card()
        self._identify_winner()
        self._retrieve_card()

    def _initiate_players(self):
        names = self._view.ask_names()
        return [Player(name) for name in names]

    def _distribute_card(self):
        for player in self._players:
            player.take_card(self._deck.draw_card())

    def _show_card(self):
        self._view.show_players_card(self._players)

    def _identify_winner(self):
        potential_winner = self._players[0]
        for player in self._players[1:]:
            potential_winner = self.player_comparator.get_winner(
                potential_winner, player
            )
        self._view.announce_winner(potential_winner)

    def _retrieve_card(self):
        for player in self._players:
            card = player.retrieve_card()
            card.hide()
            self._deck.append(card)

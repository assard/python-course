from typing import List

from CardGame.Model.Player import Player


class View:
    def ask_names(self):
        return input("Enter player name separate by , : ").split(",")

    def announce_winner(self, potential_winner):
        print(f"winner is : {potential_winner} with {potential_winner.get_card()}")

    def show_players_card(self, players: List[Player]):
        for player in players:
            print(player.get_card())

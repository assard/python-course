from CardGame.Controler.CardComparator import (
    CardComparator,
    CardComparatorHigherWinner,
    CardComparatorLowerWinner,
)
from CardGame.Controler.Controler import Controler
from CardGame.Controler.PlayerComparator import PlayerComparator
from CardGame.View.View import View

if __name__ == "__main__":
    view = View()
    card_comparator = CardComparatorHigherWinner()
    player_comparator = PlayerComparator(card_comparator)
    controller = Controler(view, player_comparator)
    controller.launch_game()
    controller.play_round()
    controller.play_round()

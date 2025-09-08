from tic_tac_toe.model.board import Board
from tic_tac_toe.view.game_view import GameView

class GameController():
    def __init__(self):
        self._board = Board()
        self._view = GameView()

    def run(self):

        while ...: # until end of game
            # Update view
            self._view.update(...)

            # Read view input
            ... = self._view.read()

            # Change model
            ... # parse input
            ... # execute move
            ... # check result
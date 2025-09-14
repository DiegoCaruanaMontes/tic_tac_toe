from tic_tac_toe.model.board import Board
from tic_tac_toe.model.game_state import GameState

from tic_tac_toe.view.game_view import GameView


class GameController:
    def __init__(self):
        self._board = Board()

    def set_view(self, view: GameView):
        self._view = view

    def run(self):
        game_state = GameState.ONGOING
        while game_state is GameState.ONGOING:  # until end of game
            # board_state = self._board.__str__()
            # Update view
            self._view.update(self._board, game_state)

            # Read view input
            x, y, player = self._view.read()

            # Change model
            valid_move, move = self._board.check_move(x, y, player)  # check move
            if valid_move:
                self._board.move(move)  # execute move
                game_state = self._board.result()  # check result

        self._view.update(self._board, game_state)

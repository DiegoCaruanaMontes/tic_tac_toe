from tic_tac_toe.model.cell import State
from tic_tac_toe.model.cell import Cell
from tic_tac_toe.model.move import Move

class Board():
    """
    Represents a 3x3 tic-tac-toe board.
    Responsible for the rules of the tic-tac-toe game.
    Manages turns, checks who wins
    """
    _board: list[list[Cell]] # [x][y]
    _turn: bool # True/False - X/O
    _size: int
    
    def __init__(self):
        self._size = 3 # Default
        self._board = [[Cell() for _ in range(self._size)] for _ in range(self._size)]
        self._turn = True

    # Function for changing the state of a particular cell
    def move(self, move: Move):
        # Check turn
        if move.check_turn(self._turn):
            # Check position in move is in range
            if move.check_range(self._size):
                # Check position in board is free
                if self._check_position_is_free(move.x, move.y):
                    # Put a piece
                    self._put_piece(move)
                    # Change turn
                    self._change_turn()

    def _check_position_is_free(self, x: int, y: int):
        return self._board[x][y].is_EMPTY()
    
    def _change_turn(self):
        self._turn = not self._turn

    def _put_piece(self, move: Move):
        self._board[move.x][move.y].set_state(State(move.player))

    # Function for checking who wins
    def result(self):
        pass
    
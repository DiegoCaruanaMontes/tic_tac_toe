from tic_tac_toe.model.state import State
from tic_tac_toe.model.cell import Cell
from tic_tac_toe.model.move import Move
from tic_tac_toe.model.game_state import GameState


class Board:
    """
    Represents a 3x3 tic-tac-toe board.
    Responsible for the rules of the tic-tac-toe game.
    Manages turns, checks who wins
    """

    _board: list[list[Cell]]  # [x][y]
    _turn: bool  # True/False - X/O
    _size: int

    def __init__(self):
        self._size = 3  # Default
        self._board = [[Cell() for _ in range(self._size)] for _ in range(self._size)]
        self._turn = True

    def check_move(self, x: int, y: int, player: bool):
        move = Move(x, y, player)

        # Check turn
        if not move.check_turn(self._turn):
            return False, None
        # Check position in move is in range
        if not move.check_range(self._size):
            return False, None
        # Check position in board is free
        if not self._check_position_is_free(move.x, move.y):
            return False, None
        return True, move

    # Function for changing the state of a particular cell
    def move(self, move: Move):
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
    def result(self) -> GameState:
        turn = State(self._turn)

        # Check rows and columns
        for i in range(0, 3):
            c = self._board[i][0].get_state()
            if (
                c != turn
                and c == self._board[i][1].get_state()
                and self._board[i][1].get_state() == self._board[i][2].get_state()
            ):
                return GameState.from_state(c)

            c = self._board[0][i].get_state()
            if (
                c != turn
                and c == self._board[1][i].get_state()
                and self._board[1][i].get_state() == self._board[2][i].get_state()
            ):
                return GameState.from_state(c)

        # Check diagonals
        c = self._board[0][0].get_state()
        if (
            c != turn
            and c == self._board[1][1].get_state()
            and self._board[1][1].get_state() == self._board[2][2].get_state()
        ):
            return GameState.from_state(c)

        c = self._board[0][2].get_state()
        if (
            c != turn
            and c == self._board[1][1].get_state()
            and self._board[1][1].get_state() == self._board[2][0].get_state()
        ):
            return GameState.from_state(c)

        # Check blank spaces
        for i in range(0, 3):
            for j in range(0, 3):
                if self._board[i][j].get_state() == State.EMPTY:
                    return GameState.from_state(State.EMPTY)

        # No winner or blank spaces -> draw
        return GameState.from_state()

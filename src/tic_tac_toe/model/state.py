from enum import Enum


class State(Enum):
    """
    Represents the state of a cell in a tic-tac-toe board
    """

    EMPTY = None
    A = True
    B = False

    def __str__(self):
        if self is State.EMPTY:
            return "-"
        elif self is State.A:
            return "X"
        elif self is State.B:
            return "O"

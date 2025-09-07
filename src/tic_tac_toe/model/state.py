from enum import Enum

class State(Enum):
    """
    Represents the state of a cell in a tic-tac-toe board
    """
    EMPTY = None
    X = True
    O = False
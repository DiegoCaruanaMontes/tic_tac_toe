from tic_tac_toe.model.state import State


class Cell:
    """
    Represents a cell in a tic-tac-toe board
    """

    _state: State

    def __init__(self):
        self._state = State.EMPTY

    def set_state(self, state: State):
        self._state = state

    def get_state(self):
        return self._state

    def is_EMPTY(self):
        return self._state == State.EMPTY

    def is_A(self):
        return self._state == State.A

    def is_B(self):
        return self._state == State.B

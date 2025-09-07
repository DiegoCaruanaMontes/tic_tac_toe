from tic_tac_toe.model.state import State

class Cell():
    """
    Represents a cell in a tic-tac-toe board
    """
    _state: State

    def __init__(self):
        self._state = State.EMPTY

    def set_state(self, state: State):
        self._state = state

    def is_EMPTY(self):
        return self._state == State.EMPTY
    
    def is_X(self):
        return self._state == State.X
    
    def is_O(self):
        return self._state == State.O


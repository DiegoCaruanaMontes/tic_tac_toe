from enum import Enum

from tic_tac_toe.model.state import State


class GameState(Enum):
    """
    Possible results of a tic-tac-toe game
    """

    ONGOING = "ONGOING"
    DRAW = "DRAW"
    A = "A"
    B = "B"

    def __str__(self):
        return self.value

    @classmethod
    def from_state(cls, state: State | None = None) -> "GameState":
        """
        Maps a State to the corresponding GameState.
        EMPTY -> ONGOING
        A -> A
        B -> B
        """
        mapping = {State.EMPTY: cls.ONGOING, State.A: cls.A, State.B: cls.B}
        return mapping.get(state, cls.DRAW)

import pytest

from tic_tac_toe.model.state import State
from tic_tac_toe.model.game_state import GameState


@pytest.mark.parametrize(
    "state",
    [
        "ONGOING",
        "DRAW",
        "A",
        "B",
    ],
)
def test_str(state):
    s = GameState(state)
    assert str(s) == state


@pytest.mark.parametrize(
    "state, expected",
    [
        (None, GameState.DRAW),
        (State.EMPTY, GameState.ONGOING),
        (State.A, GameState.A),
        (State.B, GameState.B),
    ],
)
def test_from_state(state, expected):
    assert GameState.from_state(state) is expected

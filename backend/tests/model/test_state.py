import pytest

from tic_tac_toe.model.state import State


@pytest.mark.parametrize(
    "state, expected",
    [
        (None, "-"),
        (True, "X"),
        (False, "O"),
    ],
)
def test_state_str(state, expected):
    s = State(state)
    assert str(s) == expected

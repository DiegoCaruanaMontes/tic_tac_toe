import pytest

from tic_tac_toe.model.state import State


@pytest.mark.parametrize(
    "input, expected",
    [
        (None, "-"),
        (True, "X"),
        (False, "O"),
    ],
)
def test_state_str(input, expected):
    s = State(input)
    assert str(s) == expected

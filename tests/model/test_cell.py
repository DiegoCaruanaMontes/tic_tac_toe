import pytest

from tic_tac_toe.model.state import State
from tic_tac_toe.model.cell import Cell


@pytest.mark.parametrize(
    "state, expected",
    [
        (None, "-"),
        (True, "X"),
        (False, "O"),
    ],
)
def test_state_str(state, expected):
    c = Cell()
    s = State(state)
    c.set_state(s)
    assert str(c) == expected


def test_set_state():
    cell = Cell()
    assert cell.is_EMPTY()
    cell.set_state(State.A)
    assert cell.is_A()
    cell.set_state(State.B)
    assert cell.is_B()
    cell.set_state(State.EMPTY)
    assert cell.is_EMPTY()


# def test_get_state():
#     pass

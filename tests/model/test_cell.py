from tic_tac_toe.model.state import State
from tic_tac_toe.model.cell import Cell


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

from tic_tac_toe.model.state import State
from tic_tac_toe.model.cell import Cell

def test_cell():
    cell = Cell()
    assert cell.is_EMPTY()
    cell.set_state(State.O)
    assert cell.is_O()
    cell.set_state(State.X)
    assert cell.is_X()
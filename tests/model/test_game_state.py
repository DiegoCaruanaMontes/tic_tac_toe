from tic_tac_toe.model.state import State
from tic_tac_toe.model.game_state import GameState


def test_from_state():
    assert GameState.from_state() is GameState.DRAW
    assert GameState.from_state(State.EMPTY) is GameState.ONGOING
    assert GameState.from_state(State.A) is GameState.A
    assert GameState.from_state(State.B) is GameState.B

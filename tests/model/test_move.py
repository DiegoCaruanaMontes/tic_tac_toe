import pytest
from tic_tac_toe.model.move import Move

test_data = [(0, 0, True), (0, 1, False), (1, 0, False), (2, 2, True), (2, 0, False)]


@pytest.mark.parametrize("player", [(True,), (False,)])
def test_check_turn(player):
    move = Move(0, 0, player)
    assert move.check_turn(player)


@pytest.mark.parametrize("x, y, player", test_data)
def test_check_range(x, y, player):
    move = Move(x, y, player)
    assert move.check_range(3)

from tic_tac_toe.model.move import Move

def test_check_turn():
    move = Move(0, 0, True)
    assert move.check_turn(True)
    move = Move(0, 0, False)
    assert move.check_turn(False)

def test_check_range():
    move = Move(0, 2, True)
    assert move.check_range(3)

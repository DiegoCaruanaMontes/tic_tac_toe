import pytest

from tic_tac_toe.model.move import Move
from tic_tac_toe.model.board import Board
from tic_tac_toe.model.game_state import GameState


@pytest.mark.parametrize("x1, y1, x2, y2", [(0, 0, 0, 1), (2, 0, 2, 2)])
def test_move_in_turn(x1, y1, x2, y2):
    board = Board()

    # First move A
    move = Move(x1, y1, True)
    board.move(move)
    assert not board._check_position_is_free(x1, y1)

    # A shouldn't be able to move out of its turn
    move = Move(x2, y2, True)
    board.move(move)
    assert board._check_position_is_free(x2, y2)

    # Second move B
    move = Move(x2, y2, False)
    board.move(move)
    assert not board._check_position_is_free(x2, y2)


@pytest.mark.parametrize(
    "winner, moves",
    [
        (  # Diagonal
            GameState.A,
            [(0, 0, True), (1, 0, False), (1, 1, True), (2, 0, False), (2, 2, True)],
        ),
        (  # Column
            GameState.B,
            [
                (1, 1, True),
                (0, 0, False),
                (1, 2, True),
                (0, 1, False),
                (2, 1, True),
                (0, 2, False),
            ],
        ),
        (  # Row
            GameState.A,
            [
                (0, 0, True),
                (1, 1, False),
                (1, 0, True),
                (2, 1, False),
                (2, 0, True),
            ],
        ),
        (  # Draw
            GameState.DRAW,
            [
                (0, 0, True),
                (0, 1, False),
                (1, 0, True),
                (1, 1, False),
                (2, 1, True),
                (2, 0, False),
                (2, 2, True),
                (1, 2, False),
                (0, 2, True),
            ],
        ),
    ],
)
def test_result(winner: GameState, moves: list[int, int, bool]):
    board = Board()

    # moves = [(0, 0, True), (1, 0, False), (1, 1, True), (2, 0, False), (2, 2, True)]
    print(moves)
    for m in moves:
        assert board.result() is GameState.ONGOING
        print(m)
        move = Move(*m)
        board.move(move)

    assert board.result() is winner

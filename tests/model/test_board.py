import pytest

from tic_tac_toe.model.board import Board
from tic_tac_toe.model.game_state import GameState


@pytest.mark.parametrize(
    "moves",
    [
        [
            (0, 0, True, True),
            (0, 1, False, True),
            (2, 2, False, False),
            (2, 2, True, True),
            (1, 1, True, False),
        ],
    ],
)
def test_check_move_turn(moves: list[int, int, bool, bool]):
    board = Board()
    for x, y, player, is_valid in moves:
        valid_move, m = board.check_move(x, y, player)
        assert valid_move == is_valid
        if valid_move:
            board.move(m)


@pytest.mark.parametrize("x, y", [(0, 0), (2, 2), (2, 0)])
def test_check_move_range(x, y):
    board = Board()
    valid_move, _ = board.check_move(x, y, True)
    assert valid_move


@pytest.mark.parametrize(
    "moves",
    [
        [
            (0, 0, True, True),
            (0, 1, False, True),
            (0, 0, True, False),
            (0, 1, True, False),
            (1, 1, True, True),
        ],
    ],
)
def test_check_move_position_is_free(moves: list[int, int, bool, bool]):
    board = Board()
    for x, y, player, is_valid in moves:
        valid_move, m = board.check_move(x, y, player)
        assert valid_move == is_valid
        if valid_move:
            board.move(m)


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

    for m in moves:
        assert board.result() is GameState.ONGOING
        valid_move, m = board.check_move(*m)
        assert valid_move
        board.move(m)

    assert board.result() is winner

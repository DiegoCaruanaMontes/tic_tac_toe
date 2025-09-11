import pytest

from tic_tac_toe.view.cli_game_view import CliGameView
from tic_tac_toe.model.board import Board
from tic_tac_toe.model.move import Move


# TODO: add more cases and include asserts, not just manual checking
@pytest.fixture
def prep_board():
    board = Board()
    moves = [Move(0, 0, True), Move(0, 2, False)]
    for m in moves:
        board.move(m)
    return board, board.result()


def test_update(prep_board):
    view = CliGameView()
    board, game_state = prep_board
    view.update(board, game_state)


@pytest.mark.parametrize(
    "data, expected",
    [
        (iter(["1", "2", "A"]), (1, 2, True)),
        (iter(["0", "0", "B"]), (0, 0, False)),
        (iter(["-1", "0", "2", "1", "Hello", "B"]), (2, 1, False)),
    ],
)
def test_read(monkeypatch, data, expected):
    view = CliGameView()

    monkeypatch.setattr("builtins.input", lambda _: next(data))

    result = view.read()

    assert all(a == b for a, b in zip(expected, result))

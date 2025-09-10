import pytest

from tic_tac_toe.view.cli_game_view import CliGameView


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

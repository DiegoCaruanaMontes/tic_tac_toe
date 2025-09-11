from tic_tac_toe.controller.game_controller import GameController
from tic_tac_toe.view.cli_game_view import CliGameView


def main():
    controller = GameController()
    view = CliGameView()

    controller.set_view(view)
    controller.run()


if __name__ == "__main__":
    main()

from tic_tac_toe.view.game_view import GameView
from tic_tac_toe.model.game_state import GameState


class CliGameView(GameView):
    def update(self, board_state: str, game_state: GameState):
        pass

    def read(self):
        while True:
            try:
                x = int(input("X: "))
                y = int(input("Y: "))
                if x < 0 or y < 0:
                    print("X and Y must be >= 0")
                    continue
                break
            except ValueError:
                print("X and Y must be integers")

        while True:
            player_str = input("Player (A/B): ")
            if player_str == "A":
                player = True
                break
            elif player_str == "B":
                player = False
                break
            else:
                print("Player should be A or B")

        return x, y, player

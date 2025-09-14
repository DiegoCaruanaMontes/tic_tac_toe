from abc import ABC, abstractmethod

from tic_tac_toe.model.game_state import GameState
from tic_tac_toe.model.board import Board


class GameView(ABC):
    @abstractmethod
    def update(self, board: Board, game_state: GameState):
        """
        Shows the model state
        """
        pass

    @abstractmethod
    def read(self) -> tuple[int, int, bool]:
        """
        Reads the input for a move
        """
        pass

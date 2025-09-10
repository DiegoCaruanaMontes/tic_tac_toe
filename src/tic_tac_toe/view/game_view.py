from abc import ABC, abstractmethod


class GameView(ABC):
    @abstractmethod
    def update():
        """
        Shows the model state
        """
        pass

    @abstractmethod
    def read() -> tuple[int, int, bool]:
        """
        Reads the input for a move
        """
        pass

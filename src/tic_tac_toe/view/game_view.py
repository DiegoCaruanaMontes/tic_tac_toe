from abc import ABC, abstractmethod

class GameView(ABC):

    @abstractmethod
    def update():
        pass

    @abstractmethod
    def read():
        pass
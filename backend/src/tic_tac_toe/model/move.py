class Move:
    """
    Represents the action of a player putting a piece in position (x,y)
    """

    x: int
    y: int
    player: bool

    def __init__(self, x: int, y: int, player: bool):
        self.x = x
        self.y = y
        self.player = player

    def check_turn(self, player: bool):
        return self.player == player

    def check_range(self, size: int):
        if self.x >= 0 and self.y >= 0 and self.x < size and self.y < size:
            return True

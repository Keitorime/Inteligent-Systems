

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class NoChangedTile(Tile):
    def __init__(self, x, y, empty=True, horizontal=0, vertical=0):
        super().__init__(x, y)
        # self.empty: bool = empty
        self.horizontal: int = horizontal
        self.vertical: int = vertical

class ChangedTile(Tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.result: int = 0
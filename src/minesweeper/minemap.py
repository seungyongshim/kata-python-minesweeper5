from minesweeper.mineitem import MineItem


class MineMap:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height
        self._items = [[MineItem() for x in range(width)] for y in range(height)]
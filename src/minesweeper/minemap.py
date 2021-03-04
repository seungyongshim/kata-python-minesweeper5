from typing import List, Tuple
from minesweeper.mineitem import MineItem
from toolz import pipe


class MineMap:
    def __init__(self, width: int, height: int, pos_bombs: List[Tuple[int, int]] = []):
        self._width = width
        self._height = height
        self._items = [[MineItem() for x in range(width)] for y in range(height)]

        for item in map(lambda xy: self._items[xy[1]][xy[0]], pos_bombs):
            item.set_bomb()
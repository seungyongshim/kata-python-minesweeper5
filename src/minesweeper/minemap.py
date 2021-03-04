from typing import List, Tuple
from minesweeper.mineitem import MineItem
from random import sample


class MineMap:
    def __getitem__(self, n):
        if isinstance(n, tuple):
            return self._getitem(n)
        else:
            return self._getitem(self._convert_index_int_to_tuple(n))

    def __init__(
        self, width: int, height: int, pos_bombs: List[Tuple[int, int]] = [], **kwargs
    ):
        r"""
        random_bombs : int
        """
        self._width = width
        self._height = height
        self._items = [MineItem() for _ in range(width) for _ in range(height)]

        if "random_bombs" in kwargs:
            for item in (
                self[i]
                for i in sample(range(0, width * height), kwargs["random_bombs"])
            ):
                item.set_bomb()
        else:
            for item in map(lambda xy: self._items[xy[1] * width + xy[0]], pos_bombs):
                item.set_bomb()

    def _getitem(self, xy):
        x, y = xy
        return self._items[y * self._width + x]

    def _convert_index_int_to_tuple(self, n):
        return reversed(divmod(n, self._width))

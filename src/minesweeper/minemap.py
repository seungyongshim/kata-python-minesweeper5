from typing import List, Tuple
from minesweeper.mineitem import MineItem
from random import sample


class MineMap:
    def __getitem__(self, n):
        def getitem(xy):
            x, y = xy
            return (
                None
                if x < 0 or y < 0 or x >= self._width or y >= self._height
                else self._items[y * self._width + x]
            )

        def convert_index_int_to_tuple(n):
            return reversed(divmod(n, self._width))

        if isinstance(n, tuple):
            return getitem(n)
        else:
            return getitem(convert_index_int_to_tuple(n))

    def __init__(
        self, width: int, height: int, pos_bombs: List[Tuple[int, int]] = [], **kwargs
    ):
        """
        random_bombs : int
        """
        self._width = width
        self._height = height
        self._items = [MineItem((x, y)) for x in range(width) for y in range(height)]

        def select_bomb_items():
            if "random_bombs" in kwargs:
                count = kwargs["random_bombs"]
                assert isinstance(count, int)
                return (self[i] for i in sample(range(0, width * height), count))
            else:
                return map(lambda xy: self._items[xy[1] * width + xy[0]], pos_bombs)

        for item in select_bomb_items():
            item.set_bomb()

    def near_item_generator(self, xy):
        x, y = xy

        def inner():
            yield self[(x - 1, y - 1)]
            yield self[(x, y - 1)]
            yield self[(x + 1, y - 1)]
            yield self[(x - 1, y)]
            yield self[(x + 1, y)]
            yield self[(x - 1, y + 1)]
            yield self[(x, y + 1)]
            yield self[(x + 1, y + 1)]

        return (x for x in inner() if x is not None)
    
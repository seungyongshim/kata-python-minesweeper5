from typing import List, Tuple
from minesweeper.mineitem import MineItem
from random import sample
from injector import inject


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
        self,
        width: int,
        height: int,
        pos_bombs: List[Tuple[int, int]] = [],
        random_bombs=0,
    ):
        self._width = width
        self._height = height
        self._items = [
            MineItem(self.near_items_generator((x, y)))
            for y in range(height)
            for x in range(width)
        ]

        def select_bomb_items():
            return (
                map(lambda xy: self[xy], pos_bombs)
                if random_bombs == 0
                else (self[i] for i in sample(range(0, width * height), random_bombs))
            )

        for item in select_bomb_items():
            item.set_bomb()

    def near_items_generator(self, xy):
        x, y = xy

        def nears():
            yield self[(x - 1, y - 1)]
            yield self[(x, y - 1)]
            yield self[(x + 1, y - 1)]
            yield self[(x - 1, y)]
            yield self[(x + 1, y)]
            yield self[(x - 1, y + 1)]
            yield self[(x, y + 1)]
            yield self[(x + 1, y + 1)]

        return (x for x in nears() if x is not None)

    def __str__(self):
        return "".join(str(x) for x in self._items)

    def click(self, x, y):
        self[(x, y)].click()

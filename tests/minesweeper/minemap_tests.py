from common.functools import flat_map
from minesweeper.minemap import MineMap


def test_instace():
    sut = MineMap(3, 4)

    assert sut._width is 3
    assert sut._height is 4
    assert len(list(flat_map(lambda x: x, sut._items))) is 12

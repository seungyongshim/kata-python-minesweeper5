from common.functools import flat_map
from minesweeper.minemap import MineMap


def test_instance():
    sut = MineMap(3, 4)

    assert sut._width is 3
    assert sut._height is 4
    assert len(list(flat_map(lambda x: x, sut._items))) is 12


def test_set_bombs():
    sut = MineMap(3, 4, [(0, 0), (1, 0)])
    assert sut._items[0][0].is_bomb is True
    assert sut._items[0][1].is_bomb is True

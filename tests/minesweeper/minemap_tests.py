from minesweeper.minemap import MineMap


def test_instance():
    sut = MineMap(3, 4)

    assert sut._width is 3
    assert sut._height is 4
    assert sum(1 for _ in sut._items) is 12


def test_set_bombs():
    sut = MineMap(3, 4, [(0, 0), (1, 0)])
    assert sut[(0, 0)].is_bomb is True
    assert sut[1].is_bomb is True


def test_set_bombs_random():
    sut = MineMap(3, 4, random_bombs=3)
    assert sum(1 for x in sut._items if x.is_bomb is True) == 3


def test_calculate_near_bombs_count():
    sut = MineMap(3, 4, [(0, 0)])
    assert [x.near_bombs_count for x in sut._items] == [
        0,
        1,
        0,
        1,
        1,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]

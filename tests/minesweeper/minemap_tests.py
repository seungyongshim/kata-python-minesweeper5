from minesweeper.minemap import MineMap


def test_instace():
    sut = MineMap(3, 4)

    assert sut._width is 3
    assert sut._height is 4
    assert len(sut._items) is 12

from minesweeper.mineitem import MineItem


def test_instance():
    sut = MineItem()
    assert sut


def test_is_bomb():
    sut = MineItem()
    sut.set_bomb()
    assert sut.is_bomb is True
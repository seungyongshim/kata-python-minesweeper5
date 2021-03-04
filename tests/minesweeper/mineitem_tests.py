from minesweeper.mineitem import MineItem


def test_instance():
    sut = MineItem()
    assert sut


def test_is_bomb():
    sut = MineItem()
    sut.set_bomb()
    sut.click()
    assert sut.is_bomb is True
    assert str(sut) == "*"


def test_near_bombs_count():
    sut = MineItem()
    sut.near_bombs_count = 7
    sut.click()
    assert str(sut) == "7"


def test_is_cover():
    sut = MineItem()
    assert str(sut) == "."

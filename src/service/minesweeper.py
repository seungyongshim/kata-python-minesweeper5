from typing import Any, NewType

from injector import inject
from minesweeper.minemap import MineMap
import uuid

Session = NewType("SessionFactory", Any)

mine_maps = {}


def check_available_mine_map(session):
    if "mine_map" in session:
        if session["mine_map"] in mine_maps.keys():
            return True

    return False


class MineSweeperService:
    @inject
    def __init__(self, session: Session):
        self._session = session

        if check_available_mine_map(session) is False:
            session["mine_map"] = uuid.uuid1()
            mine_maps[session["mine_map"]] = MineMap(3, 3, random_bombs=3)

        self.mine_map = mine_maps[session["mine_map"]]

    def __str__(self):
        l = str(self.mine_map)
        return l

    def click(self, x: int, y: int):
        self.mine_map.click(x, y)

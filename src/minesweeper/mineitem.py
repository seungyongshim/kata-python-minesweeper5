class MineItem:
    _is_bomb: bool
    near_bombs_count: int

    def set_bomb(self):
        self._is_bomb = True

    @property
    def is_bomb(self):
        return self._is_bomb

    def __str__(self) -> str:
        return str(self.near_bombs_count)
class MineItem:
    _is_bomb: bool

    def set_bomb(self):
        self._is_bomb = True

    @property
    def is_bomb(self):
        return self._is_bomb
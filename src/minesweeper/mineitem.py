class MineItem:
    _is_bomb: bool = False
    _is_cover: bool = True
    near_bombs_count: int = 0

    def __init__(self, near_items=()):
        self.near_items = near_items

    def set_bomb(self):
        self._is_bomb = True
        for item in self.near_items:
            item.near_bombs_count += 1

    @property
    def is_bomb(self):
        return self._is_bomb

    def __str__(self):
        if self._is_cover:
            return "."
        if self.is_bomb:
            return "*"
        return str(self.near_bombs_count)

    def click(self):
        if self._is_cover is False:
            return
        self._is_cover = False

        if self.near_bombs_count is 0:
            for item in self.near_items:
                item.click()
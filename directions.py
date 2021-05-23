from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

    def get_opposite(self):
        if self is self.UP:
            return self.DOWN
        elif self is self.DOWN:
            return self.UP
        elif self is self.RIGHT:
            return self.LEFT
        elif self is self.LEFT:
            return self.RIGHT

    def convert(self):
        if self is self.UP:
            return 0, -1
        elif self is self.DOWN:
            return 0, 1
        elif self is self.RIGHT:
            return 1, 0
        elif self is self.LEFT:
            return -1, 0
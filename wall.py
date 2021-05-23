from random import randrange


class Wall:
    """Represents a wall between nodes"""

    def __init__(self, direction):
        self.direction = direction
        self.value = randrange(1, 1000)

    def get_value(self):
        return self.value

    def __str__(self):
        obj = (self.direction, self.value)
        return str(obj)

    def __repr__(self):
        obj = (self.direction, self.value)
        return str(obj)

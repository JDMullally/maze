from wall import Wall
from directions import Direction


class Node:
    """Represents a Node"""

    def __init__(self, row, col, size):
        self.position = (row, col)
        self.size = size
        self.knocked_walls = []
        self.walls = []
        for d in Direction:
            self.walls.append(Wall(d))

    def contains_side(self, direction):
        for wall in self.walls:
            if wall.direction is direction:
                return True
        return False

    def get_possible_moves(self):
        moves = []
        if self.position[0] - 1 > 0 and self.contains_side(Direction.LEFT):
            moves.append(Direction.LEFT)
        if self.position[1] - 1 > 0 and self.contains_side(Direction.UP):
            moves.append(Direction.UP)
        if self.position[0] + 1 < self.size and self.contains_side(Direction.RIGHT):
            moves.append(Direction.RIGHT)
        if self.position[1] + 1 < self.size and self.contains_side(Direction.DOWN):
            moves.append(Direction.DOWN)
        return moves

    def knock_down_wall(self, direction):
        removed = None
        for wall in self.walls:
            if wall.direction == direction:
                removed = wall
                break
        self.walls.remove(removed)
        self.knocked_walls.append(removed)

    def return_wall(self, direction):
        for wall in self.walls:
            if wall.direction is direction:
                return wall

    def __str__(self):
        obj = (self.position, self.walls.__str__())
        return str(obj)

    def __repr__(self):
        obj = (self.position, self.walls.__str__())
        return str(obj)


from wall import Wall
from directions import Direction


class Node:
    """Represents a Node"""

    def __init__(self, row, col, size):
        """Init function"""
        self.position = (row, col)
        self.size = size
        self.knocked_walls = []
        self.walls = []
        self.visited = False
        for d in Direction:
            self.walls.append(Wall(d))

    def get_pos(self):
        return self.position

    def contains_side(self, direction):
        """Checks if the node still has the """
        for wall in self.walls:
            if wall.direction is direction:
                return True
        return False

    def visit(self):
        self.visited = True

    def get_visited(self):
        return self.visited

    def get_possible_moves(self):
        """Gets all the possible directions that can be made from the node's current coordinates"""
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
        """Knocks down the wall in the given direction if there are less than two knocked down walls"""
        removed = None
        for wall in self.walls:
            if wall.direction == direction:
                removed = wall
                break
        self.walls.remove(removed)
        self.knocked_walls.append(removed)

    def return_wall(self, direction):
        """Returns the wall object in the given direction relative to the node"""
        for wall in self.walls:
            if wall.direction is direction:
                return wall

    def __str__(self):
        """str method"""
        obj = (self.position, self.walls.__str__())
        return str(obj)

    def __repr__(self):
        """repr method"""
        obj = (self.position, self.walls.__str__())
        return str(obj)


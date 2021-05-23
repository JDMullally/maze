from node import Node


# TODO fix generation

class Maze:
    """Represents the entire maze"""

    def __init__(self, size):
        self.maze = {}
        self.unspanned = []
        self.spanned = []
        self.size = size
        self.total_size = size * size
        self.generate_maze(size)
        self.create_spanning_tree()

    """Generates a 1D list of length size^2 that contains all node and their 4 walls 
    and a list of nodes that are not in the spanning tree"""

    def generate_maze(self, size):
        for r in range(size):
            for c in range(size):
                self.maze[(r, c)] = (Node(r, c, size))
                self.unspanned.append((r, c))

    """Creates a spanning tree using the generated nodes"""

    def create_spanning_tree(self):
        first = self.unspanned.pop(0)
        self.spanned.append(first)
        while len(self.spanned) != self.total_size:
            paths = {}
            for coord in self.spanned:
                paths[coord] = self.maze[coord].get_possible_moves()
            self.check_paths(paths)

    """Checks the possible paths that can be taken and constructs a list of potential moves"""

    def check_paths(self, paths):
        potential_moves = []
        for key, val in paths.items():
            for dir in val:
                r_diff, c_diff = dir.convert()
                new_key = (key[0] + r_diff, key[1] + c_diff)
                from_obj = self.maze[key]
                to_obj = self.maze[new_key]
                total_weight = from_obj.return_wall(dir).get_value() \
                               + to_obj.return_wall(dir.get_opposite()).get_value()
                potential_moves.append((key, new_key, dir, total_weight))
        self.choose_move(potential_moves)

    """Chooses a move using Prims MST Algorithm"""

    def choose_move(self, potential_moves):
        min_val = 2001
        from_coord = None
        to_coord = None
        from_wall = None
        for move in potential_moves:
            if move[3] < min_val and not self.spanned.__contains__(move[1]):
                min_val = move[3]
                from_coord = move[0]
                to_coord = move[1]
                from_wall = move[2]
        if len(potential_moves) == 0 or from_wall is None:
            print('error')
            self.__str__()
            return
        to_wall = from_wall.get_opposite()
        if self.unspanned.__contains__(to_coord):
            self.unspanned.remove(to_coord)
            self.spanned.append(to_coord)
        self.maze[from_coord].knock_down_wall(from_wall)
        self.maze[to_coord].knock_down_wall(to_wall)

    """str method"""

    def __str__(self):
        for val in self.maze.values():
            print(val)

    """Returns a dictionary of maze location and remaining walls after Prims MST Algo has been triggered"""

    def create_drawable_maze(self):
        drawable_maze = {}
        for key, val in self.maze.items():
            drawable_maze[key] = val.walls
        return drawable_maze

    """Returns a dictionary of maze locations and walls that have been knocked which act as paths for a player"""

    def create_navigable_maze(self):
        navigable_maze = {}
        for key, val in self.maze.items():
            navigable_maze[key] = val.knocked_walls
        return navigable_maze

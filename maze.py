from node import Node
import functools
import operator

foldr = lambda func, acc, xs: functools.reduce(lambda x, y: func(y, x), xs[::-1], acc)


class Maze:
    """Represents the entire maze"""

    def __init__(self, size):
        """init function which"""
        self.maze = {}
        self.size = size
        self.next_unvisited_node = None
        self.total_size = size * size
        self.generate_maze(size)
        self.create_spanning_tree()

    def generate_maze(self, size):
        """Generates a 1D list of length size^2 that contains all node and their 4 walls
           and a list of nodes that are not in the spanning tree"""
        for r in range(size):
            for c in range(size):
                self.maze[(r, c)] = (Node(r, c, size))
                # self.unspanned.append((r, c)

    def create_spanning_tree(self):
        """Creates a spanning tree using the generated nodes"""
        visited_nodes = list(map(Node.get_visited, list(self.maze.values())))
        while not foldr(operator.and_, True, visited_nodes):
            self.visit_node(visited_nodes)
            visited_nodes = list(map(Node.get_visited, list(self.maze.values())))

    def visit_node(self, visited_nodes):
        """Chooses a the next reachable node, pops it from the list, and chooses the cheapest path to a new node.
        If there have been no visits, the initial node is chosen, destroys the cheapest wall and
        adds the now reachable neighbor to the list. """
        ignore_visit = False
        if foldr(operator.or_, False, visited_nodes) and self.next_unvisited_node:
            """Standard condition trying to find the next best move"""
            print(self.next_unvisited_node)
            self.next_unvisited_node.visit()
            moves = self.next_unvisited_node.get_possible_moves()

        elif self.next_unvisited_node is None and foldr(operator.or_, False, visited_nodes):
            """Hit a dead end and we need to find a new starting point"""
            for item in list(self.maze.values()):
                if not item.get_visited():
                    self.next_unvisited_node = item
                    break
            self.next_unvisited_node.visit()
            ignore_visit = True
            moves = self.next_unvisited_node.get_possible_moves()
        else:
            """Initial Condition starting at (0,0)"""
            self.next_unvisited_node = self.maze[(0, 0)]
            self.next_unvisited_node.visit()
            moves = self.next_unvisited_node.get_possible_moves()
        self.check_moves(moves, ignore_visit)

    def check_moves(self, moves, ignore_visit):
        """Checks the possible paths that can be taken and constructs a list of potential moves"""
        key = self.next_unvisited_node.get_pos()
        potential_moves = {}
        for move in moves:
            r_diff, c_diff = move.convert()
            to_key = (key[0] + r_diff, key[1] + c_diff)
            if self.maze[to_key].get_visited() and not ignore_visit:
                continue
            else:
                from_obj = self.maze[key]
                to_obj = self.maze[to_key]
                total_weight = from_obj.return_wall(move).get_value() \
                               + to_obj.return_wall(move.get_opposite()).get_value()
                potential_moves[(key, to_key, move)] = total_weight
        self.choose_move(potential_moves)

    def choose_move(self, potential_moves):
        """Chooses a move using DFS to create a MST"""
        if len(potential_moves) == 0:
            self.next_unvisited_node = None
        else:
            min = 2001
            for pot_min in potential_moves.values():
                if min > pot_min:
                    min = pot_min
            min_key = list(potential_moves.keys())[list(potential_moves.values()).index(min)]
            from_key = min_key[0]
            to_key = min_key[1]
            from_move = min_key[2]
            to_move = from_move.get_opposite()
            print(from_key, to_key, from_move, to_move)
            self.maze[from_key].knock_down_wall(from_move)
            self.maze[to_key].knock_down_wall(to_move)
            self.next_unvisited_node = self.maze[to_key]

    def __str__(self):
        """str method"""
        for val in self.maze.values():
            print(val)

    def create_drawable_maze(self):
        """Returns a dictionary of maze location and remaining walls after Prims MST Algo has been triggered"""
        drawable_maze = {}
        for key, val in self.maze.items():
            drawable_maze[key] = val.walls
        return drawable_maze

    def create_navigable_maze(self):
        """Returns a dictionary of maze locations and walls that have been knocked which act as paths for a player"""
        navigable_maze = {}
        for key, val in self.maze.items():
            navigable_maze[key] = val.knocked_walls
        return navigable_maze

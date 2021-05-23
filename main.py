import pygame
from directions import Direction
from maze import Maze
import sys


# Starts the game by drawing the maze and
def draw_grid(window_size, color, screen, size):
    rect = pygame.Rect((0, 0), (window_size, window_size))
    pygame.draw.rect(screen, color, rect, 3)
    val = window_size/size
    for i in range(size):
        pygame.draw.line(screen, color, (0, i*val), (window_size, i*val), 3)
        pygame.draw.line(screen, color, (i * val, 0), (i * val, window_size), 3)


def destroy_walls(screen, color, window_size, size, nav):
    val = window_size / size
    coordinates = nav.keys()
    rects = []
    for coordinate in coordinates:
        row, col = coordinate[0], coordinate[1]
        directions = nav.get(coordinate)
        for direction in directions:
            proper_dir = direction.direction
            tuple_dir = proper_dir.convert()
            if proper_dir is Direction.DOWN:
                rect = pygame.Rect(col * val + 2, row * val + val/2 + 2, val - 3, val)
                rects.append(rect)
            elif proper_dir is Direction.UP:
                rect = pygame.Rect((col + 1) * val + 2, row * val + val / 2 + 2, val - 3, val)
                rects.append(rect)
            elif proper_dir is Direction.RIGHT:
                rect = pygame.Rect(col * val + val/2 + 2, row * val + 2, val, val - 3)
                rects.append(rect)
            elif proper_dir is Direction.LEFT:
                rect = pygame.Rect(col * val + val/2 + 2, (row + 1) * val + 2, val, val - 3)
                rects.append(rect)
    for rect in rects:
        pygame.draw.rect(screen,
                         color,
                           rect, 0)


def start(nav, size):
    # Define some colors
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    pygame.init()
    window_size = 500
    window_dimensions = (window_size, window_size)
    screen = pygame.display.set_mode(window_dimensions)

    pygame.display.set_caption("Maze Game")

    done = False

    clock = pygame.time.Clock()

    screen.fill(white)

    draw_grid(window_size, black, screen, int(size))
    destroy_walls(screen, white, window_size, int(size), nav)
    # -------- Main Program Loop -----------
    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.flip()

        clock.tick(60)

    # Close the window and quit.
    pygame.quit()


if __name__ == '__main__':
    size = int(sys.argv[1])
    maze = Maze(size)
    # maze.__str__()
    draw = maze.create_drawable_maze()
    nav = maze.create_navigable_maze()
    start(nav, size)

from window import Window
from maze import Maze
from geometry import Point, Line, Box

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
WINDOW_TITLE = "Maze Solver"


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    rows = 12
    cols = 16
    margin = 50
    box_width = (SCREEN_WIDTH - 2 * margin) // cols
    box_height = (SCREEN_HEIGHT - 2 * margin) // rows

    maze = Maze(margin, margin, rows, cols, box_width, box_height, window)
    maze.solve()

    window.redraw_while_active()


if __name__ == '__main__':
    main()

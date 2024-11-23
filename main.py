from window import Window
from geometry import Point, Line, Box

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
WINDOW_TITLE = "Maze Solver"


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

    box1 = Box(
        True, True, True, True,
        400, 1200, 225, 675
    )

    window.draw_box(box1, "red", 2)

    window.redraw_while_active()


if __name__ == '__main__':
    main()

from window import Window
from geometry import Point, Line, Box

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
WINDOW_TITLE = "Maze Solver"


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

    box1 = Box(
        True, True, True, False,
        400, 700, 225, 675
    )

    box2 = Box(
        True, True, False, True,
        900, 1200, 225, 675
    )

    window.draw_box(box1, "black", 2)
    window.draw_box(box2, "black", 2)
    window.draw_path(box1, box2, False)

    # line = Line(Point(550, 450), Point(1050, 450))
    # window.draw_line(line)

    window.redraw_while_active()


if __name__ == '__main__':
    main()

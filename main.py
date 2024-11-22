from window import Window
from geometry import Point, Line

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
WINDOW_TITLE = "Maze Solver"


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

    p1 = Point(0, 0)
    p2 = Point(SCREEN_WIDTH, SCREEN_HEIGHT)
    line1 = Line(p1, p2)

    p3 = Point(SCREEN_WIDTH, 0)
    p4 = Point(0, SCREEN_HEIGHT)
    line2 = Line(p3, p4)

    window.draw_line(line1, "red", 8)
    window.draw_line(line2, "black")

    window.redraw_while_active()


if __name__ == '__main__':
    main()

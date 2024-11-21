from window import Window

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
WINDOW_TITLE = "Maze Solver"


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    window.redraw_while_active()


if __name__ == '__main__':
    main()

from window import Window

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900


def main():
    window = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.redraw_while_active()


if __name__ == '__main__':
    main()

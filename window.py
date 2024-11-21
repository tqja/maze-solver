from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__active = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def redraw_while_active(self):
        self.__active = True
        while self.__active:
            self.redraw()

    def close(self):
        self.__active = False

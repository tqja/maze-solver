from tkinter import Tk, BOTH, Canvas


class Window:
    """ Tkinter window class """
    def __init__(self, width: int, height: int, title: str) -> None:
        self.__root = Tk()
        self.__root.title(title)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__active = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        """ Redraws the Tkinter window. """
        self.__root.update_idletasks()
        self.__root.update()

    def redraw_while_active(self) -> None:
        """ Continually redraws the Tkinter window while active. """
        self.__active = True
        while self.__active:
            self.redraw()

    def close(self) -> None:
        """ Closes the Tkinter window by setting the active member to False. """
        self.__active = False

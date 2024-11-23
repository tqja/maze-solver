from tkinter import Tk, BOTH, Canvas
from geometry import Line, Box


class Window:
    """ Tkinter window class """
    def __init__(self, width: int, height: int, title: str) -> None:
        self.__root = Tk()
        self.__root.title(title)
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__active = False

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

    def draw_line(self, line: Line, colour: str = "black", width: int = 2) -> None:
        """
        Draws a given Line object on the canvas.
        :param line: The Line object to draw.
        :param colour: The colour of the line.
        :param width: The width of the line.
        """
        line.draw(self.__canvas, colour, width)

    def draw_box(self, box: Box, colour: str = "black", width: int = 2) -> None:
        """
        Draws a given Box object on the canvas.
        :param box: The Box object to draw.
        :param colour: The colour of the box lines.
        :param width: The width of the box lines.
        """
        box.draw(self.__canvas, colour, width)

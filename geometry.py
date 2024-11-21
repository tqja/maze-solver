from tkinter import Canvas


class Point:
    """ Representation of a point on the screen. """
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line:
    """ Representation of a line on the screen. """
    def __init__(self, p1: Point, p2: Point) -> None:
        self.__p1 = p1
        self.__p2 = p2

    def draw(self, canvas: Canvas, colour: str, width: int = 2) -> None:
        """
        Draws a line on the given Canvas object.
        :param canvas: The canvas object to draw the line on.
        :param colour: The fill colour of the line.
        :param width: The width of the line.
        """

        canvas.create_line(
            self.__p1.x, self.__p1.y,
            self.__p2.x, self.__p2.y,
            fill=colour, width=width
        )

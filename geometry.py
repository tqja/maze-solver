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


class Box:
    """ Box shape with up to 4 sides. """
    def __init__(self, up: bool, down: bool, left: bool, right: bool,
                 x1: int, x2: int, y1: int, y2: int) -> None:
        self.__up = up
        self.__down = down
        self.__left = left
        self.__right = right
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def draw(self, canvas: Canvas, colour: str, width: int = 2) -> None:
        """
        Draws a box with up to 4 sides on the given Canvas object.
        :param canvas: The canvas object to draw the line on.
        :param colour: The fill colour of the line.
        :param width: The width of the line.
        """
        p1 = Point(self.__x1, self.__y1)
        p2 = Point(self.__x2, self.__y1)
        p3 = Point(self.__x1, self.__y2)
        p4 = Point(self.__x2, self.__y2)

        if self.__up:
            Line(p1, p2).draw(canvas, colour, width)
        if self.__down:
            Line(p3, p4).draw(canvas, colour, width)
        if self.__left:
            Line(p1, p3).draw(canvas, colour, width)
        if self.__right:
            Line(p2, p4).draw(canvas, colour, width)

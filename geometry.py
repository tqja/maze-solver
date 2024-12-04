from tkinter import Canvas
from typing import Tuple


class Point:
    """ Representation of a point on the screen. """
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'


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

    def __repr__(self):
        return f"Line(\n    {self.__p1},\n    {self.__p2}\n)"


class Box:
    """ Box shape with up to 4 sides. """
    def __init__(self, window, x1: int, x2: int, y1: int, y2: int) -> None:
        self.up = True
        self.down = True
        self.left = True
        self.right = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__window = window
        self.visited = False

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

        blank = "#f0f0f0"
        c = colour if self.up else blank
        Line(p1, p2).draw(canvas, c, width)

        c = colour if self.down else blank
        Line(p3, p4).draw(canvas, c, width)

        c = colour if self.left else blank
        Line(p1, p3).draw(canvas, c, width)

        c = colour if self.right else blank
        Line(p2, p4).draw(canvas, c, width)

    def draw_path(self, canvas: Canvas, box, backtrack: bool = False) -> None:
        """
        Draws a path from the center of this box to the center of the given box.
        :param canvas: The canvas to draw the path on.
        :param box: The box to draw the path to.
        :param backtrack: Whether to display a backtracking path (red).
        """
        xm, ym = self.get_mid_coords()
        box_xm, box_ym = box.get_mid_coords()

        colour = "red" if backtrack else "blue"
        p1 = Point(xm, ym)
        p2 = Point(box_xm, box_ym)
        path = Line(p1, p2)

        path.draw(canvas, colour)

    def get_mid_coords(self) -> Tuple[int, int]:
        xm = self.__x1 + (self.__x2 - self.__x1) // 2
        ym = self.__y1 + (self.__y2 - self.__y1) // 2
        return xm, ym

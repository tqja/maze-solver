import time
from random import seed, randrange

from geometry import Box
from window import Window


class Maze:
    def __init__(self, x: int, y: int, rows: int, cols: int, cell_width: int, cell_height: int, window: Window):
        seed(0)
        self.__x = x
        self.__y = y
        self.__rows = rows
        self.__cols = cols
        self.__box_width = cell_width
        self.__box_height = cell_height
        self.__window = window
        self.__boxes = []

        # maze setup
        self._init_boxes()
        self._generate_start_end()
        self._make_path(0, 0)
        self._reset_visited()

    def _init_boxes(self) -> None:
        for i in range(self.__cols):
            col = []
            for j in range(self.__rows):
                x1 = self.__x + i * self.__box_width
                y1 = self.__y + j * self.__box_height
                col.append(
                    Box(
                        self.__window,
                        x1,
                        x1 + self.__box_width,
                        y1,
                        y1 + self.__box_height
                    )
                )
            self.__boxes.append(col)
        for i in range(self.__cols):
            for j in range(self.__rows):
                self._draw_box(i, j)

    def _draw_box(self, col: int, row: int) -> None:
        if not self.__window:
            return
        self.__window.draw_box(self.__boxes[col][row])
        self._animate()

    def _animate(self) -> None:
        if not self.__window:
            return
        self.__window.redraw()
        time.sleep(0.005)

    def _generate_start_end(self) -> None:
        self.__boxes[0][0].up = False
        self.__boxes[-1][-1].down = False
        self.__window.draw_box(self.__boxes[0][0])
        self.__window.draw_box(self.__boxes[-1][-1])
        self._animate()

    def _make_path(self, row, col):
        self.__boxes[row][col].visited = True
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while True:
            unvisited = []
            for di, dj in directions:
                ni = row + di
                nj = col + dj
                if (
                        0 <= ni < self.__cols and
                        0 <= nj < self.__rows and
                        not self.__boxes[ni][nj].visited
                ):
                    unvisited.append((ni, nj))

            if not unvisited:
                self.__window.draw_box(self.__boxes[row][col])
                return

            next_col, next_row = unvisited[randrange(len(unvisited))]

            if next_col == row - 1:
                self.__boxes[row][col].left = False
                self.__boxes[row - 1][col].right = False
            elif next_col == row + 1:
                self.__boxes[row][col].right = False
                self.__boxes[row + 1][col].left = False
            elif next_row == col - 1:
                self.__boxes[row][col].up = False
                self.__boxes[row][col - 1].down = False
            elif next_row == col + 1:
                self.__boxes[row][col].down = False
                self.__boxes[row][col + 1].up = False

            self.__window.draw_box(self.__boxes[row][col])
            self._animate()

            self._make_path(next_col, next_row)

    def _reset_visited(self) -> None:
        for col in range(self.__cols):
            for row in range(self.__rows):
                self.__boxes[col][row].visited = False

    def solve(self):
        self._solve_r(0, 0)

    def _solve_r(self, col, row) -> bool:
        self._animate()
        self.__boxes[col][row].visited = True

        if col == self.__cols - 1 and row == self.__rows - 1:
            return True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dCol, dRow in directions:
            current = self.__boxes[col][row]
            # box in bounds
            if 0 <= col + dCol < self.__cols and 0 <= row + dRow < self.__rows:
                if ((dCol == -1 and not current.left and not self.__boxes[col + dCol][row].visited) or
                        (dCol == 1 and not current.right and not self.__boxes[col + dCol][row].visited)):
                    self.__window.draw_path(current, self.__boxes[col + dCol][row])
                    if self._solve_r(col + dCol, row):
                        return True
                    self.__window.draw_path(self.__boxes[col + dCol][row], current, True)
                elif ((dRow == -1 and not current.up and not self.__boxes[col][row + dRow].visited) or
                        (dRow == 1 and not current.down and not self.__boxes[col][row + dRow].visited)):
                    self.__window.draw_path(current, self.__boxes[col][row + dRow])
                    if self._solve_r(col, row + dRow):
                        return True
                    self.__window.draw_path(self.__boxes[col][row + dRow], current, True)
        return False

from tkFileDialog import askopenfile
from subprocess import check_output
from copy import deepcopy
from bisect import insort


class Cell:

    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Cell):
            p = self.number == other.number
            return p
        if isinstance(other, int):
            return self.number == other
        return False

    def __lt__(self, other):
        if isinstance(other, Cell):
            return self.number < other.number
        return False

    def __str__(self):
        return str(self.number)

    def __repr__(self):
        return str(self.number)


class NpuzzleBoard:
    _sorted_array = []
    _values_size = None
    _size = None
    _g = 0
    _h_functions = []

    def __init__(self, board_file, heuristic_function=None):
        self._solved = False
        self._parent = None
        self._puzzle = []
        self.puzzle_as_list = None
        self._final_weight = None
        self.generation = 0

        if heuristic_function:
            self._h_functions += heuristic_function

        if isinstance(board_file, NpuzzleBoard):
            self.__dict__.update(deepcopy(board_file.__dict__))
        elif isinstance(board_file, str):
            self._create_board(board_file.split('\n'))
        else:
            self._create_board(board_file.readlines())

        if not self._values_size:
            self._values_size = self._size ** 2


        if not self._sorted_array:
            sorted_puzzle = list(self.go_by_order())
            self._sorted_array += [i for i in range(1, self._values_size + 1)]
            self._sorted_array[self._values_size - 1] = 0
            self._sorted_cells = [Cell(number, sorted_puzzle[i].x, sorted_puzzle[i].y) for i, number in enumerate(self._sorted_array)]
        if not self._final_weight:
            self._final_weight = self._get_final_weight()



    def _create_board(self, board_lines):
        y = 0
        self._null_x = None
        self._null_y = None

        for line in board_lines:
            if line and line != '\n' and not line.startswith("#"):
                line = line.split("#")[0]
                if not self._size:
                    self._size = int(line)
                else:
                    row = line.split()
                    if len(row) != self._size:
                        raise ValueError
                    int_row = []
                    for x_index, number in enumerate(row):
                        number = int(number)
                        if number == 0:
                            self._null_x = x_index
                        cell = Cell(number, x_index, y)
                        int_row.append(cell)
                    y += 1
                    self._puzzle.append(int_row)
        self._null_y = self._get_null_row()

    def _get_null_row(self):
        for i in range(self._size):
            if 0 in self._puzzle[i]:
                return i

    def go_by_order(self):
        cur_size = self._size - 1
        cur_rev_size = 0
        counter = self._size ** 2
        reverse = False
        x = 0
        y = 0
        count_error = counter % 2 == 1

        while True:
            while (not reverse and x < cur_size) or (reverse and x > cur_rev_size):
                yield self._puzzle[y][x]
                counter -= 1
                x = x - 1 if reverse else x + 1
            if not counter:
                break
            while (not reverse and y < cur_size) or (reverse and y > cur_rev_size):
                yield self._puzzle[y][x]
                counter -= 1
                y = y - 1 if reverse else y + 1
            if reverse:
                x += 1
                y += 1
                cur_rev_size += 1
                cur_size -= 1
            if count_error and counter == 1:
                yield self._puzzle[y][x]
                break
            reverse = not reverse

    def is_solved(self):
        return self._solved

    def __str__(self):
        result = [" ".join(str(el.number) for el in line) for line in self._puzzle]
        return str("\n".join(result)) + "\n" + str(self._final_weight)

    def _update_generation(self):
        self._g += 1

    def _get_final_weight(self, coords=None):
        if self._final_weight is None:
            self._final_weight = 0
        for func in self._h_functions:

             self._final_weight += func(self, coords=coords)

        return  self._final_weight + self.generation

    def _get_dist(self, cell, const_cell):
        return abs(cell.x - const_cell.x) + abs(cell.y - const_cell.y)


    def _new_board_with(self, null_x, null_y):
        new_null_x = null_x + self._null_x
        new_null_y = null_y + self._null_y

        if 0 <= new_null_x < self._size and 0 <= new_null_y < self._size:
            new_board = NpuzzleBoard(self)
            new_board._puzzle[self._null_y][self._null_x].number, new_board._puzzle[new_null_y][new_null_x].number = \
                new_board._puzzle[new_null_y][new_null_x].number, new_board._puzzle[self._null_y][self._null_x].number
            number = new_board._puzzle[self._null_y][self._null_x]
            new_board._final_weight = self._final_weight
            new_board._get_final_weight(coords=(number, null_x, null_y))
            new_board._null_x = new_null_x
            new_board._null_y = new_null_y
            new_board._parent = self
            new_board.generation = self.generation + 1
            return new_board


    def get_available_boards(self):
        boards = []
        val = [-1, 0, 1, 0, -1]
        for i in range(4):
            inner_new_board = self._new_board_with(val[i], val[i+1])
            if inner_new_board:
                boards.append(inner_new_board)
        return boards

    def __eq__(self, other):
        if isinstance(other, NpuzzleBoard):
            return str(other._puzzle) == str(self._puzzle)
        return False

    def __lt__(self, other):
        if isinstance(other, NpuzzleBoard):
            return self._final_weight < other._final_weight
        return False

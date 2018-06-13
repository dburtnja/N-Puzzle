from tkFileDialog import askopenfile
from subprocess import check_output


class NpuzzleBoard:
    _sorted_array = None
    _values_size = None
    _size = None

    def __init__(self, board_file):
        self._number_of_wrong_elements = None
        self._parent = None
        self._puzzle = []
        if isinstance(board_file, NpuzzleBoard):
            self.__dict__.update(board_file.__dict__)
        elif isinstance(board_file, str):
            self._create_board(board_file.split('\n'))
        else:
            self._create_board(board_file.readlines())
        if not self._sorted_array:
            self._values_size = self._size ** 2
            self._sorted_array = [i for i in range(1, self._values_size + 1)]
            self._sorted_array[self._values_size - 1] = 0

    def _create_board(self, board_lines):
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
                        int_row.append(number)
                    self._puzzle.append(int_row)
        self._null_y = self._get_null_row()

    def _get_null_row(self):
        for i in range(self._size):
            if 0 in self._puzzle[i]:
                return i

    def get_number_of_wrong_elements(self):
        diff_elements = 0
        for index, element in enumerate(self.go_by_order()):
            if self._sorted_array[index] != element:
                diff_elements += 1
        return diff_elements

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

    def is_solvable(self):
        if self._size % 2 == 0:
            ordered_puzzle = sum(self._puzzle, [])
        else:
            ordered_puzzle = list(self.go_by_order())
        my_sum = 0

        for i in range(self._size ** 2):
            my_sum += len([n for n in ordered_puzzle[i:] if n < ordered_puzzle[i] and n != 0])
        if self._size % 2 == 0:
            return (my_sum + self._null_y + 1) % 2 == 0
        else:
            return my_sum % 2 == 0

    def __str__(self):
        result = [" ".join(str(el) for el in line) for line in self._puzzle]
        return str("\n".join(result))

    def _change_null(self, new_null_x, new_null_y):
        if new_null_x != self._null_x:
            print("x")
            print(self)
            self._puzzle[self._null_y][new_null_x], self._puzzle[self._null_y][self._null_x] = \
                self._puzzle[self._null_y][self._null_x], self._puzzle[self._null_y][new_null_x]
            self._null_x = new_null_x
            print(self)
        if new_null_y != self._null_y:
            print("y")
            print(self)
            self._puzzle[new_null_y][self._null_x], self._puzzle[self._null_y][self._null_x] =\
                self._puzzle[self._null_y][self._null_x], self._puzzle[new_null_y][self._null_x]
            self._null_y = new_null_y
            print(self)

    def _new_board_with(self, null_x, null_y):
        new_null_x = null_x + self._null_x
        new_null_y = null_y + self._null_y

        if 0 <= new_null_x < self._size and 0 <= new_null_y < self._size:
            new_board = NpuzzleBoard(self)
            new_board._change_null(new_null_x, new_null_y)
            return new_board

    def get_available_boards(self):
        boards = []
        val = [-1, 0, 1, 0, -1]
        for i in range(4):
            iner_new_board = self._new_board_with(val[i], val[i+1])
            if iner_new_board:
                boards.append(iner_new_board)
        return boards



if __name__ == "__main__":
    generate = True
    if generate:
        out = check_output(['python', 'npuzzle-gen.py', '3'])
        print(out)
        board = NpuzzleBoard(out)
    else:
        puzzle_file = askopenfile()
        board = NpuzzleBoard(puzzle_file)
    if not board.is_solvable():
        print("This puzzle is unsolvable")
    print("Number not placed elements: {}".format(board.get_number_of_wrong_elements()))
    print(board)
    for new_board in board.get_available_boards():
        print('\n')
        print(new_board)



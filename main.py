from tkFileDialog import askopenfile
from subprocess import check_output


class NpuzzleBoard:

    def __init__(self, board_file):
        self._puzzle = []
        self._size = 0
        try:
            if isinstance(board_file, str):
                self._create_board(board_file.split('\n'))
            else:
                self._create_board(board_file.readlines())
        except:
            print("Error on creation board")
        self._values_size = self._size ** 2
        self._sorted_array = [i for i in range(1, self._values_size + 1)]
        self._sorted_array[self._values_size - 1] = 0


    def _create_board(self, board_lines):
        for line in board_lines:
            if line and line != '\n' and not line.startswith("#"):
                line = line.split("#")[0]
                if not self._size:
                    self._size = int(line)
                else:
                    row = line.split()
                    if len(row) != self._size:
                        raise ValueError
                    self._puzzle.append([int(number) for number in row])

    def get_empty_position_row(self):
        for row in range(self._size):
            if 0 in self._puzzle[row]:
                return row

    def get_empty_position_column(self):
        row = self.get_empty_position_row()
        for col in range(self._size):
            if 0 == self._puzzle[row][col]:
                return col

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

    # def _iterate(self, reverse, horizontal, x, y, i):
    #     if not reverse:
    #         while x <
    #
    #
    # def go_by_order(self):
    #     reverse = False
    #     x = 0
    #     y = 0
    #     i = self._size ** 2
    #
    #     while i > 0:
    #         self._iterate()

    def is_solvable(self):
        if self._size % 2 == 0:
            ordered_puzzle = sum(self._puzzle, [])
        else:
            ordered_puzzle = list(self.go_by_order())
        empty_index = ordered_puzzle.index(0)
        print(empty_index)
        my_sum = 0

        for i in range(self._size ** 2):
            # print(ordered_puzzle[i:])
            l = len([n for n in ordered_puzzle[i:] if n < ordered_puzzle[i] and n != 0])
            # print(l)
            my_sum += l
        if self._size % 2 == 0:
            empty_row_position = self.get_empty_position_row() + 1
            print("row nbr: " + str(empty_row_position))
            print("sum: " + str(my_sum))
            return (my_sum + empty_row_position) % 2 == 0
        else:
            return my_sum % 2 == 0

    def __str__(self):
        return str(self._puzzle)


if __name__ == "__main__":
    generate = True
    if generate:
        out = check_output(['python', 'npuzzle-gen.py', '6'])
        print(out)
        board = NpuzzleBoard(out)
    else:
        puzzle_file = askopenfile()
        board = NpuzzleBoard(puzzle_file)
    if not board.is_solvable():
        print("This puzzle is unsolvable")
    print("Number not placed elements: {}".format(board.get_number_of_wrong_elements()))
    # print(board)
    x = 0
    y = 0
    size = board._size - 1
    round = 0
    while (size > 0):
        for i in range(0, size - round):
            print (board._puzzle[x][y])
            y = y + 1
        for i in range(0, size - round):
            print (board._puzzle[x][y])
            x = x + 1
        for i in range(round, size):
            print (board._puzzle[x][y])
            y = y - 1
        for i in range(round, size):
            print (board._puzzle[x][y])
            x = x - 1
        x += 1
        y += 1
        size -= 1
        round += 1
    if board._size % 2:
        print(board._puzzle[x - 1][y - 1])

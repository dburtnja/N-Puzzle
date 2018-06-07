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

    def get_empty_position_sum(self):
        x = 0
        y = 0
        while (x < self._size):
            while (y < self._size):
                if (self._puzzle[x][y] == 0):
                    print ("POS =  " + str((x*self._size + y) // self._size  + 1))
                    return (((x*self._size) - 1) // self._size + 1)
                y += 1
            x+=1
            y = 0


    def get_empty_position_column(self):
        row = self.get_empty_position_row()
        for col in range(self._size):
            if 0 == self._puzzle[row][col]:
                return col

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
        ordered_puzzle = list(self.go_by_order())
        my_sum = 0

        for i in range(self._size ** 2):
            print(ordered_puzzle[i:])
            l = len([n for n in ordered_puzzle[i:] if n < ordered_puzzle[i] and n != 0])
            print(l)
            my_sum += l
        if self._size % 2 == 0:
            # empty_row_position = self.get_empty_position_row() + 1
            empty_row_position = self.get_empty_position_sum()
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
        out = check_output(['python', 'npuzzle-gen.py', '4'])
        print(out)
        board = NpuzzleBoard(out)
    else:
        puzzle_file = askopenfile()
        board = NpuzzleBoard(puzzle_file)
    if not board.is_solvable():
        print("This puzzle is unsolvable")
    print(board)

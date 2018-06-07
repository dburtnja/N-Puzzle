from tkFileDialog import askopenfile


class NpuzzleBoard:

    def __init__(self, board_file):
        self._puzzle = []
        self._size = 0
        try:
            self._create_board(board_file.readlines())
        except:
            print("Error on creation board")

    def _create_board(self, board_lines):
        for line in board_lines:
            if line != '\n' and not line.startswith("#"):
                line = line.split("#")[0]
                if not self._size:
                    self._size = int(line)
                else:
                    row = line.split()
                    if len(row) != self._size:
                        raise ValueError
                    self._puzzle.append([int(number) for number in row])

    def get_empty_position(self):
        for row in range(self._size):
            if 0 in self._puzzle[row]:
                for col in range(self._size):
                    if self._puzzle[row][col] == 0:
                        return row, col

    def is_solvable(self):
        cur_size = self._size - 1
        cur_rev_size = 0
        counter = self._size ** 2
        reverse = False
        x = 0
        y = 0
        count_error = True if counter % 2 == 1 else False

        while True:
            while (not reverse and x < cur_size) or (reverse and x > cur_rev_size):
                print(self._puzzle[y][x])
                counter -= 1
                x = x - 1 if reverse else x + 1
            if not counter:
                break
            while (not reverse and y < cur_size) or (reverse and y > cur_rev_size):
                print(self._puzzle[y][x])
                counter -= 1
                y = y - 1 if reverse else y + 1
            if reverse:
                x += 1
                y += 1
                cur_rev_size += 1
                cur_size -= 1
            if count_error and counter == 1:
                print(self._puzzle[y][x])
                break
            reverse = not reverse
        return True

    def __str__(self):
        return str(self._puzzle)


if __name__ == "__main__":
    puzzle_file = askopenfile()
    board = NpuzzleBoard(puzzle_file)
    if not board.is_solvable():
        print("This puzzle isn't solvable")
    print(board)

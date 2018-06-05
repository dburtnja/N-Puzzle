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
            if not line.startswith("#"):
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
        print(self.get_empty_position())
        return True

    def __str__(self):
        return str(self._puzzle)


if __name__ == "__main__":
    puzzle_file = askopenfile()
    board = NpuzzleBoard(puzzle_file)
    if not board.is_solvable():
        print("This puzzle isn't solvable")
    print(board)

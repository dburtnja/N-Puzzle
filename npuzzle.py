from sys import argv
from NpuzzleBoard import *
from argparse import ArgumentParser
from time import time
from heuristic_functions import get_heuristic
from os import system


def generate_puzzle(heuristic_func):
    print "npuzzle-gen.py [-h] [-s] [-u] [-i ITERATIONS] size"
    print "press enter to set: 'npuzzle-gen.py 3"
    npuzzle_gen = raw_input("npuzzle-gen.py ")
    if not npuzzle_gen:
        npuzzle_gen = ['3']
    else:
        npuzzle_gen = npuzzle_gen.split()
    out = check_output(['python', 'npuzzle-gen.py'] + npuzzle_gen)
    print out
    return NpuzzleBoard(out, heuristic_func)


def read_from_file(heuristic_func):
    puzzle_file = askopenfile()
    return NpuzzleBoard(puzzle_file, heuristic_func)


def solve_puzzle(board):
    opened = [board]
    closed = []
    opened_i = 0
    all_i = 0


    while opened:
        current = opened.pop(0)
        if current.is_solved():
            return current
        insort(closed, current)
        for new_board in current.get_available_boards():
            all_i += 1
            if new_board not in closed and new_board not in opened:
                insort(opened, new_board)
                opened_i += 1
    print "Total number of states ever selected in the 'opened' set: {}".format(opened_i)
    print "Maximum number of states ever represented in memory at the same time during the search {}".format(all_i)


def get_selected_heuristics(argv):
    h_functions = get_heuristic()
    if set(argv) - set(h_functions.keys()) <= 0:
        return [h_function for key, h_function in h_functions.items()]
    return [h_function for key, h_function in h_functions.items() if key in argv]


def is_solvable(board):
    ordered_puzzle = sum(board._puzzle, [])
    row = abs((ordered_puzzle.index(0) / board._size) - board._size)
    my_sum = 0

    if ((board._size - 2) / 4) % 2 == 1:
        my_sum += 1
    for i in range(board._size ** 2):
        my_sum += len([n.number for n in ordered_puzzle[i:] if n < ordered_puzzle[i] and n.number != 0])
    if board._size % 2 == 0:
        if row % 2 == 0:
            return my_sum % 2 != 0
        else:
            return my_sum % 2 == 0
    else:
        return my_sum % 2 != 0


if __name__ == "__main__":
    available_flags = {
        "-g": "Puzzle generated from npyzzle-gen.py (default)",
        "-f": "Read puzzle from file",
        "-m": "Heuristic: Manhattan-distance",
        "-p": "Heuristic: Misplaced titles",
        "-o": "Heuristic: Wrong rows and columns",
        "-h": "Print usage" #TODO
    }
    argv = argv[1:]
    if len(set(argv) - set(available_flags.keys())) > 0:
        for arg in argv:
            if arg not in available_flags.keys():
                print "Flag {} doesn't support".format(arg)
    # try:
    h_functions = get_selected_heuristics(argv)
    print h_functions

    if '-f' in argv:
        board = read_from_file(h_functions)
    else:
        board = generate_puzzle(h_functions)

    if is_solvable(board):
        t = time()
        final_board = solve_puzzle(board)
        print "TIME = " + str(time() - t)
        result = []

        while final_board._parent:
            result.append(final_board)
            final_board = final_board._parent
        print "Number of moves required to transition from the initial state to the final state," \
              "according to the search: {}".format(len(result))
        for result_board in result[::-1]:
            system('clear')
            print result_board
    else:
        print("This puzzle is unsolvable")
    # except:
    #     print("This puzzle unsolvable")
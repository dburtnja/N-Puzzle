#include <iostream>
#include "Cell.hpp"
#include "PuzzleReader.hpp"


int main() {
    Cell    cell(9, 8, 8);
    std::cout << "Hello, World!" << cell << std::endl;
    PuzzleReader reader;

    std::cout << reader.runCommand("python ../../npuzzle-gen.py -s 3");
//    std::cout << reader.runCommand("ls ../..");

    return 0;
}
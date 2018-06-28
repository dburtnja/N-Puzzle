#include <iostream>
#include "Cell.hpp"
#include "PuzzleReader.hpp"


int main() {
    Cell    cell(9, 8, 8);
    std::cout << "Hello, World!" << cell << std::endl;
    PuzzleReader reader;

//    reader.getFromCommand("python ../../npuzzle-gen.py -s 3");
    reader.getFromFile("../test.txt");
//    std::cout << reader.runCommand("ls ../..");

    return 0;
}
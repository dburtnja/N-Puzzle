//
// Created by ezburde on 27.06.2018.
//

#include "PuzzleReader.hpp"

PuzzleReader::PuzzleReader() = default;

PuzzleReader::~PuzzleReader() = default;

PuzzleReader::PuzzleReader(PuzzleReader const &obj) {
    *this = obj;
}

PuzzleReader &PuzzleReader::operator=(PuzzleReader const &obj) {
    return *this;
}

std::vector<Cell> &PuzzleReader::getFromCommand(std::string const &command) {
    std::string file_name = "temp.txt";
    std::system((command + " > " + file_name).c_str()); // redirect output to file
    return _createVectorFromFile(file_name);
}

std::vector<Cell> &PuzzleReader::_createVectorFromFile(std::string const &filename) {

    // open file for input, return string containing characters in the file
    std::ifstream file(filename) ;
    return { std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>() } ;
}

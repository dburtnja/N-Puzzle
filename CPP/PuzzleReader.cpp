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
    std::string file_name = ".temp.txt";
    std::system((command + " > " + file_name).c_str()); // redirect output to file
    return _createVectorFromFile(file_name);
}

std::vector<Cell> &PuzzleReader::_createVectorFromFile(std::string const &filename) {
    std::vector<Cell> puzzle;
    // open file for input, return string containing characters in the file
    std::ifstream file(filename) ;
    std::string result = { std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>() } ;
    std::istringstream  lines(result);
    std::vector<std::string>    linesWithoutComment;

    for (std::string line; std::getline(lines, line, '\n');) {
        if (line.rfind('#', 0) == 0)
            continue;
        this->_splitString(line, '#', linesWithoutComment);
        if (!linesWithoutComment.empty())
            line = linesWithoutComment[0];
        std::cout << line;
    }
    return puzzle;
}

std::vector<Cell> &PuzzleReader::getFromFile(std::string const & filename) {
    return _createVectorFromFile(filename);
}

void PuzzleReader::_splitString(std::string input, char delimiter, std::vector<std::string> &result) {
    std::istringstream          lines(input);

    for (std::string line; std::getline(lines, line, delimiter);)
        if (!line.empty())
            result.push_back(line);
}

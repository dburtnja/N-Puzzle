//
// Created by ezburde on 27.06.2018.
//

#ifndef CPP_PUZZLEREADER_HPP
#define CPP_PUZZLEREADER_HPP


#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include "Cell.hpp"
#include <sstream>

class PuzzleReader {
private:
    std::vector<Cell>   &_createVectorFromFile(std::string const &filename);
    void _splitString(std::string input, char delimiter, std::vector<std::string> &result);

public:
    PuzzleReader();
    ~PuzzleReader();
    PuzzleReader(PuzzleReader const & obj);

    PuzzleReader &operator=(PuzzleReader const & obj);
    std::vector<Cell>   &getFromCommand(std::string const & command);
    std::vector<Cell>   &getFromFile(std::string const & filename);

};


#endif //CPP_PUZZLEREADER_HPP

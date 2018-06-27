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

class PuzzleReader {
private:
    std::vector<Cell>   &_createVectorFromFile(std::string const &filename);

public:
    PuzzleReader();
    ~PuzzleReader();
    PuzzleReader(PuzzleReader const & obj);

    PuzzleReader &operator=(PuzzleReader const & obj);
    std::vector<Cell>   &getFromCommand(std::string const & command);
};


#endif //CPP_PUZZLEREADER_HPP

//
// Created by ezburde on 27.06.2018.
//

#ifndef CPP_NPUZZLEBOARD_HPP
#define CPP_NPUZZLEBOARD_HPP


#include <vector>
#include "Cell.hpp"

class NpuzzleBoard {
private:
    std::vector<Cell>   _puzzle
    short               _size;
    NpuzzleBoard();

public:
    NpuzzleBoard(std::vector<Cell> _puzzle, short size);
    ~NpuzzleBoard();
};


#endif //CPP_NPUZZLEBOARD_HPP

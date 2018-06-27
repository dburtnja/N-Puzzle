//
// Created by ezburde on 27.06.2018.
//

#ifndef CPP_CELL_HPP
#define CPP_CELL_HPP

#include <ostream>

class Cell {
private:
    short   _number;
    short   _x;
    short   _y;
    Cell();

public:
    Cell(short const & number, short const & x, short const & y);
    ~Cell();
    Cell(Cell const & obj);

    Cell    &operator=(Cell const & obj);
    bool    operator==(Cell const & obj);
    bool    operator==(short const & number);

    short   getNumber() const;
};

std::ostream &	operator<<(std::ostream & o, Cell const & obj);

#endif //CPP_CELL_HPP

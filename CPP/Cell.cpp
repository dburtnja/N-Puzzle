//
// Created by ezburde on 27.06.2018.
//

#include "Cell.hpp"

Cell::Cell() = default;

Cell::~Cell() = default;

Cell::Cell(short const &number, short const &x, short const &y) :
    _number(number), _x(x), _y(y)
{
}

Cell::Cell(Cell const &obj) {
    *this = obj;
}

Cell &Cell::operator=(Cell const &obj) {
    if (this == &obj)
        return *this;
    this->_number = obj._number;
    this->_x = obj._x;
    this->_y = obj._y;
    return *this;
}

bool Cell::operator==(Cell const &obj) {
    if (this == &obj)
        return true;
    return this->_number == obj._number;
}

bool Cell::operator==(const short &number) {
    return this->_number == number;
}

short Cell::getNumber() const {
    return this->_number;
}


std::ostream &operator<<(std::ostream &o, Cell const &obj) {
    o << obj.getNumber();
    return o;
}

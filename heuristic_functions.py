
def manhattan_distance(self):
    final_dist = 0
    diff_elements = 0

    for cell in self.go_by_order():
        for const_cel in self._sorted_cells:
            if cell.number == const_cel.number:
                if cell.number != 0:
                    final_dist += self._get_dist(cell, const_cel)
                break
    if diff_elements == 0:
        self._solved = True
    return final_dist + diff_elements


def misplaced_tiles(self):
    diff_elements = 0

    for cell in self.go_by_order():
        for const_cel in self._sorted_cells:
            if cell.number == const_cel.number and cell.number != 0:
                if (cell.x, cell.y) != (const_cel.x, const_cel.y):
                    diff_elements += 1
                break
    if diff_elements == 0:
        self._solved = True
    return diff_elements


def out_of_row_and_colomns(self):
    row = 0
    col = 0

    for cell in self.go_by_order():
        for const_cel in self._sorted_cells:
            if cell.number == const_cel.number and cell.number != 0:
                if cell.x != const_cel.x:
                    row +=1
                if cell.y != const_cel.y:
                    col += 1
                break
    return row + col


def get_heuristic():
    return {
        '-m': manhattan_distance,
        '-p': misplaced_tiles,
        '-o': out_of_row_and_colomns
    }
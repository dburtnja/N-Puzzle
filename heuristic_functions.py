
def manhattan_distance(self):
    final_dist = 0
    diff_elements = 0

    for cell in self.go_by_order():
        for const_cel in self._sorted_cells:
            if cell.number == const_cel.number:
                if (cell.x, cell.y) != (const_cel.x, const_cel.y):
                    diff_elements += 1
                if cell.number != 0:
                    final_dist += self._get_dist(cell, const_cel)
                break
    if diff_elements == 0:
        self._solved = True
    return final_dist + diff_elements
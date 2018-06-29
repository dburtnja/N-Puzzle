
# def manhattan_distance(self, coords=None):
#     final_dist = 0
#
#     for cell in self.go_by_order():
#         for const_cel in self._sorted_cells:
#             if cell.number == const_cel.number:
#                 if cell.number != 0:
#                     final_dist += self._get_dist(cell, const_cel)
#                 break
#
#     if final_dist == 0:
#         self._solved = True
#     return final_dist


def manhattan_distance(self, coords=None):
    final_dist = 0
    if coords:
        final_num = next((x for x in self._sorted_cells if x == coords[0]), None)

        manhattan_delta = abs(final_num.x - coords[0].x) + abs(final_num.y - coords[0].y)
        manhattan_delta1 = abs(final_num.x - coords[0].x - coords[1]) + abs(final_num.y - coords[0].y - coords[2])
        final_man_delta = manhattan_delta1 - manhattan_delta
        if self._final_weight - final_man_delta == 0:
            self._solved = True
        return -final_man_delta
    else:
        for cell in self.go_by_order():
            for const_cel in self._sorted_cells:
                if cell.number == const_cel.number:
                    if cell.number != 0:
                        final_dist += self._get_dist(cell, const_cel)
                    break

    if final_dist == 0:
        self._solved = True
    return final_dist


def misplaced_tiles(self, coords=None):
    diff_elements = 0
    old = self._final_weight

    for cell in self.go_by_order():
        for const_cel in self._sorted_cells:
            if cell.number == const_cel.number and cell.number != 0:
                if (cell.x, cell.y) != (const_cel.x, const_cel.y):
                    diff_elements += 1
                break
    if diff_elements == 0:
        self._solved = True
    return diff_elements - old

def out_of_row_and_colomns(self, coords=None):
    row = 0
    col = 0
    old = self._final_weight

    for cell in self.go_by_order():
        for const_cel in self._sorted_cells:
            if cell.number == const_cel.number and cell.number != 0:
                if cell.x != const_cel.x:
                    row +=1
                if cell.y != const_cel.y:
                    col += 1
                break
    if row + col == 0:
        self._solved = True
    return row + col - old


def get_heuristic():
    return {
        '-m': manhattan_distance,
        '-p': misplaced_tiles,
        '-o': out_of_row_and_colomns
    }
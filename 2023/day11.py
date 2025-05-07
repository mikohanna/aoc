#!/usr/bin/env python3

GALAXIES = []
GALAXY_COORDS = []
EMPTY_ROWS = []
EMPTY_COLS = []

def print_galaxies():
    for line in GALAXIES:
        print("".join(line))

def set_galaxies():
    with open("src/day11.txt") as f:
        for i, line in enumerate(f):
            line = line.strip()
            GALAXIES.append(line)
            if not "#" in line:
                EMPTY_ROWS.append(i)
    find_empty_cols()

def change_row_col(m):
    new_m = []
    for i in range(len(m[0])):
        line = []
        for j in range(len(m)):
            line.append(m[j][i])
        new_m.append(line)
    return new_m


def find_empty_cols():
    new_galaxies = change_row_col(GALAXIES)
    for i, line in enumerate(new_galaxies):
        if "#" not in line:
            EMPTY_COLS.append(i)

def find_coords():
    for i, line in enumerate(GALAXIES):
        for j, c in enumerate(line):
            if c == '#':
                GALAXY_COORDS.append((i, j))

def path_counter(expansion_rate):
    path_sum = 0
    for i, c1 in enumerate(GALAXY_COORDS):
        for c2 in GALAXY_COORDS[i+1:]:
            path = abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])
            path += path_grower(c1, c2, expansion_rate)
            path_sum += path
    return path_sum

def path_grower(coord1, coord2, expansion_rate):
    grower = 0
    for i in range(min(coord1[0], coord2[0]) + 1, max(coord1[0], coord2[0])):
        if i in EMPTY_ROWS:
            grower += expansion_rate - 1
    for i in range(min(coord1[1], coord2[1]) + 1, max(coord1[1], coord2[1])):
        if i in EMPTY_COLS:
            grower += expansion_rate - 1

    return grower





def main():
    set_galaxies()
    find_coords()
    print("the answer for part 1: ", path_counter(2))
    print("the answer for part 2: ", path_counter(1000000))



if __name__ == "__main__":
    main()
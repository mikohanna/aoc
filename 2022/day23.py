#!/usr/bin/env python3

def move_one_step(crds, direction):
    row, col = crds
    if direction == 0:       #north
        return [row-1, col]
    if direction == 1:       #south
        return [row+1, col]
    if direction == 2:       #west
        return [row, col-1]
    if direction == 3:       #east
        return [row, col+1]

def set_direction(is_empty, direction): #returns an int (0-3), 0: move to north, 1: move to south, 2: move to west, 3: move to east 
    if direction == 0:
        if all(is_empty[:3]): #to north
            return 0
        elif all(is_empty[4:7]): #to south
            return 1
        elif all(is_empty[-2:]) and is_empty[0]: #to west
            return 2
        elif all(is_empty[2:5]): #to east
            return 3
    elif direction == 1:
        if all(is_empty[4:7]): #to south
            return 1
        elif all(is_empty[-2:]) and is_empty[0]: #to west
            return 2
        elif all(is_empty[2:5]): #to east
            return 3
        elif all(is_empty[:3]): #to north
            return 0
    elif direction == 2:
        if all(is_empty[-2:]) and is_empty[0]: #to west
            return 2
        elif all(is_empty[2:5]): #to east
            return 3
        elif all(is_empty[:3]): #to north
            return 0
        elif all(is_empty[4:7]): #to south
            return 1
    elif direction == 3:
        if all(is_empty[2:5]): #to east
            return 3
        elif all(is_empty[:3]): #to north
            return 0
        elif all(is_empty[4:7]): #to south
            return 1
        elif all(is_empty[-2:]) and is_empty[0]: #to west
            return 2
    return -1


def get_coords_to_move(coords, direction): #direction -> 0: north, 1: south, 2: west, 3: east
    crds_to_move = []
    for crd in coords:
        row, col =  crd 
        is_empty = [[row-1, col-1] not in coords, #clockwise: NW - N - NE - E - SE - S - SW - W /// north[:3], south[4:7], west[0,-2,-1], east[2:5] 
                    [row-1, col] not in coords,
                    [row-1, col+1] not in coords,
                    [row, col+1] not in coords,
                    [row+1, col+1] not in coords,
                    [row+1, col] not in coords,
                    [row+1, col-1] not in coords,
                    [row, col-1] not in coords]
        dr = set_direction(is_empty, direction)
        if all(is_empty) or dr == -1:
            # print("all empty... ", row, col)
            crds_to_move.append([crd, crd])
            continue
        crds_to_move.append([crd, move_one_step(crd,dr)])
    return crds_to_move

def move_steps(crds_to_move):
    crds = []
    new_coords = [crd[1] for crd in crds_to_move]
    for curr_crd, new_crd in crds_to_move:
        if new_coords.count(new_crd) > 1:
            crds.append(curr_crd)
        else:
            crds.append(new_crd)
    return crds

#for part 1:
def rounds(coords, roundnum):
    direction = 0
    for i in range(roundnum):
        crds_to_move = get_coords_to_move(coords, direction)
        coords = move_steps(crds_to_move)
        direction += 1
        if direction == 4:
            direction = 0
    return coords

#for part 2:
def rounds2(coords):
    direction = 0
    prev_coords = []
    round_cnt = 0
    while prev_coords != coords:
        crds_to_move = get_coords_to_move(coords, direction)
        prev_coords = coords
        coords = move_steps(crds_to_move)
        direction += 1
        if direction == 4:
            direction = 0
        round_cnt += 1
    return round_cnt


def get_minmax_coords(coords):
    min_coords = [100000, 100000]
    max_coords = [-100000, -100000]
    for row, col in coords:
        if row > max_coords[0]:
            max_coords[0] = row
        if row < min_coords[0]:
            min_coords[0] = row
        if col > max_coords[1]:
            max_coords[1] = col
        if col < min_coords[1]:
            min_coords[1] = col
    return min_coords + max_coords

def get_answer_part1(coords):
    min_row, min_col, max_row, max_col = get_minmax_coords(coords)
    return (max_row - min_row + 1) * (max_col - min_col + 1) - len(coords)

#for testing purposes
def print_elves(coords):
    min_row, min_col, max_row, max_col = get_minmax_coords(coords)
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if [i, j] in coords:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()
        

def main():
    coords = []
    with open("src/day23.txt") as f:
        for i, l in enumerate(f):
            coords += [[i, j] for j, c in enumerate(l.rstrip()) if c == '#']
    final_coord = rounds(coords, 10)
    print("the answer for part 1: ", get_answer_part1(final_coord)) #3864
    print("the answer for part 2: ", rounds2(coords)) #946 --- but it's slooooowwwwwww... (it takes approx. 18 minutes)


if __name__ == '__main__':
    main()


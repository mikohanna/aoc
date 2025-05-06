#!/usr/bin/env python3

def set_direction(prev_dir, actual_dir, is_even):
    if is_even:
        if prev_dir == 'U':
            return actual_dir
        else:
            return 'R' if actual_dir == 'L' else 'L'
    else:
        if prev_dir == 'R':
            return 'U' if actual_dir == 'L' else 'D'
        else:
            return 'D' if actual_dir == 'L' else 'U'

def get_coord(coords):
    coord = [0, 0]
    direction = 'U'
    for i, crd in enumerate(coords):
        direction = set_direction(direction, crd[0], not i%2)
        if direction == 'R':
            coord[0] += int(crd[1:])
        if direction == 'L':
            coord[0] -= int(crd[1:])
        if direction == 'U':
            coord[1] += int(crd[1:])
        if direction == 'D':
            coord[1] -= int(crd[1:])
    dist = abs(coord[0]) + abs(coord[1])
    return dist

def get_coords_2(direction_list):
    direction = 'U'
    coords = [[0, 0],]
    for index, dr in enumerate(direction_list):
        direction = set_direction(direction, dr[0], not index%2)
        last_cord = coords[-1]
        for i in range(int(dr[1:])):
            if direction == 'R':
                new_crd = [last_cord[0] + i + 1, last_cord[1]]
                if new_crd in coords:
                    return abs(new_crd[0]) + abs(new_crd[1])
                coords.append(new_crd)
            if direction == 'L':
                new_crd = [last_cord[0] - i - 1, last_cord[1]]
                if new_crd in coords:
                    return abs(new_crd[0]) + abs(new_crd[1])
                coords.append(new_crd)
            if direction == 'U':
                new_crd = [last_cord[0], last_cord[1] + i + 1]
                if new_crd in coords:
                    return abs(new_crd[0]) + abs(new_crd[1])
                coords.append(new_crd)
            if direction == 'D':
                new_crd = [last_cord[0], last_cord[1] - i - 1]
                if new_crd in coords:
                    return abs(new_crd[0]) + abs(new_crd[1])
                coords.append(new_crd)

def main():
    input_list = open("src/day1.txt").read().split(", ")
    print("the answer for part 1: ", get_coord(input_list))
    print("the answer for part 2: ", get_coords_2(input_list))


if __name__ == "__main__":
    main()

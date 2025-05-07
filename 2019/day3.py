#!/usr/bin/env python3

def get_wire_data(filename):
    data = open(filename).read().split("\n")
    wire0 = [(s[0], int(s[1:])) for s in data[0].split(",")]
    wire1 = [(s[0], int(s[1:])) for s in data[1].split(",")]
    return (wire0, wire1)


def get_coordinates(instructions):
    actual = [0, 0]
    coordinates = []
    for ins, num in instructions:
        if ins == 'R':
            for i in range(actual[0] + 1, actual[0] + num + 1):
                coordinates.append((i, actual[1]))
            actual[0] += num
        if ins == 'L':
            for i in range(actual[0] - 1, actual[0] - num - 1, -1):
                coordinates.append((i, actual[1]))
            actual[0] -= num
        if ins == 'U':
            for i in range(actual[1] + 1, actual[1] + num + 1):
                coordinates.append((actual[0], i))
            actual[1] += num
        if ins == 'D':
            for i in range(actual[1] - 1, actual[1] - num - 1, -1):
                coordinates.append((actual[0], i))
            actual[1] -= num
    return coordinates


#part1
def get_distance(filename):
    wire0, wire1 = get_wire_data(filename)
    coord0 = set(get_coordinates(wire0))
    coord1 = set(get_coordinates(wire1))
    return min([abs(c[0]) + abs(c[1]) for c in coord0 if c in coord1])


#part2
def get_steps(filename):
    wire0, wire1 = get_wire_data(filename)
    # wire0 = [('R', 8), ('U', 5), ('L', 5), ('D', 3)]
    # wire1 = [('U', 7), ('R', 6), ('D', 4), ('L', 4)]
    coord0 = get_coordinates(wire0)
    coord1 = get_coordinates(wire1)
    coord0_set = set(coord0)
    coord1_set = set(coord1)
    same_coords = coord0_set.intersection(coord1_set)
    intersect_steps = []
    for c in same_coords:
        if intersect_steps and c[0] > intersect_steps[-1][0] and c[1] > intersect_steps[-1][1]:
            break
        intersect_steps.append((coord0.index(c) + 1, coord1.index(c) + 1))
    return min([i[0] + i[1] for i in intersect_steps])
    
    


def main():
    print("The answer for part 1: ", get_distance("src/day3.txt"))
    print("The answer for part 2: ", get_steps("src/day3.txt"))

main()
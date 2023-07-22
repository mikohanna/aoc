#!/usr/bin/env python3

LINE_LENGTH = 1000
# LINE_LENGTH = 10

def print_grid(grid): #only for testing!
    for i, g in enumerate(grid):
        if i != 0 and i % LINE_LENGTH == 0:
            print()
        print(g, end=" ")
    print()
    print("-" * 100)
        

def change_grid(grid, turn, start, end):
    size = [(end[0] - start[0] + 1), (end[1] - start[1] + 1)] #size of columns, size of rows
    for i in range(size[0]):
            for j in range(size[1]):
                index = ((start[0] + i) * LINE_LENGTH + start[1]) + j
                if turn == "on":
                    grid[index] = 1
                elif turn == "off":
                    grid[index] = 0
                else:
                    if grid[index] == 1:
                        grid[index] = 0
                    else:
                        grid[index] = 1
    return grid


def change_grid_advanced(grid, turn, start, end):
    size = [(end[0] - start[0] + 1), (end[1] - start[1] + 1)] #size of columns, size of rows
    for i in range(size[0]):
            for j in range(size[1]):
                index = ((start[0] + i) * LINE_LENGTH + start[1]) + j
                if turn == "on":
                    grid[index] += 1
                elif turn == "off":
                    if grid[index] > 0:
                        grid[index] -= 1
                else:
                    grid[index] += 2
    return grid


def light_grid(filename, is_part_2=False):
    grid = [0] * LINE_LENGTH ** 2
    f = open(filename)
    for line in f:
        line = line.rstrip('\n').split()
        if line[0] == "toggle":
            turn = "toggle"
            start = [int(n) for n in line[1].split(",")]
            end = [int(n) for n in line[3].split(",")]
        else:
            turn = line[1]
            start = [int(n) for n in line[2].split(",")]
            end = [int(n) for n in line[4].split(",")]
        if is_part_2:
            grid = change_grid_advanced(grid, turn, start, end)
        else:
            grid = change_grid(grid, turn, start, end)
    return sum(grid)


def main():
    print("The answer for part 1: ", light_grid("src/day6.txt")) #377891
    print("The answer for part 2: ", light_grid("src/day6.txt", is_part_2=True)) #14110788



if __name__ == "__main__":
    main()
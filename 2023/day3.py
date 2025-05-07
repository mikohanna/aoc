#!/usr/bin/env python3

import re

SCHEMATIC = []

def set_schematic():
    with open("src/day3.txt") as f:
        for line in f:
            SCHEMATIC.append(line.strip())

#for part 1
def check_row(row, start, end):
    if start == 0:
        return SCHEMATIC[row][end] != '.'
    if end == len(SCHEMATIC[row]):
        return SCHEMATIC[row][start - 1] != '.'
    return SCHEMATIC[row][start - 1] != '.' or SCHEMATIC[row][end] != '.'

#for part 1
def check_col(row, start, end): #with adjacents
    if start:
        start -= 1
    if end < len(SCHEMATIC[row]) - 1:
        end += 1
    upper = "" if row == 0 else SCHEMATIC[row - 1][start : end]
    lower = "" if row == len(SCHEMATIC) - 1 else SCHEMATIC[row + 1][start : end]
    upper = re.sub("\d+|\.+", "", upper)
    lower = re.sub("\d+|\.+", "", lower)
    return upper or lower

#for part 2
def num_finder(index):
    num = []
    for c in reversed(SCHEMATIC[index[0]][:index[1]]):
        if not c.isdigit():
            break
        num.append(c)
        num.reverse()
    for c in SCHEMATIC[index[0]][index[1]:]:
        if not c.isdigit():
            break
        num.append(c)
    return int("".join(num))
        

#for part 2
def gear_num_finder(row, col):
    if row == 0 or row == len(SCHEMATIC) - 1:
        if row == 0:
            up = ""
        else:
            down = ""
    elif col == 0:
        up = SCHEMATIC[row - 1][:2]
        down = SCHEMATIC[row + 1][:2]
    elif col == len(SCHEMATIC[row]) - 1:
        up = SCHEMATIC[row - 1][col - 1:]
        down = SCHEMATIC[row + 1][col - 1:]
    else:
        up = SCHEMATIC[row - 1][col - 1 : col + 2]
        down = SCHEMATIC[row + 1][col - 1 : col + 2]
    left = "" if col == 0 else SCHEMATIC[row][col - 1]
    right = "" if col == len(SCHEMATIC[row]) - 1 else SCHEMATIC[row][col + 1]

    indexes = []
    if up[0].isdigit():
        indexes.append((row - 1, col - 1))
        if not up[1].isdigit() and up[2].isdigit():
            indexes.append((row - 1, col + 1))
    elif up[1].isdigit():
        indexes.append((row - 1, col))
    elif up[2].isdigit():
        indexes.append((row - 1, col + 1))
    if down[0].isdigit():
        indexes.append((row + 1, col - 1))
        if not down[1].isdigit() and down[2].isdigit():
            indexes.append((row + 1, col + 1))
    elif down[1].isdigit():
        indexes.append((row + 1, col))
    elif down[2].isdigit():
        indexes.append((row + 1, col + 1))
 
    if left.isdigit():
        indexes.append((row, col - 1))
    if right.isdigit():
        indexes.append((row, col + 1))

    if len(indexes) == 2:
        return num_finder(indexes[0]) * num_finder(indexes[1])
    return 0

#for part 1 and 2
def find_part_nums():
    num_sum = 0
    num_sum_pt_2 = 0
    for i, line in enumerate(SCHEMATIC):
        matches = re.finditer("\d+", line)
        for match in matches:
            start, end = match.span()
            if check_row(i, start, end) or check_col(i, start, end):
                num_sum += int(match.group())
        matches = re.finditer("\*+", line)
        for match in matches:
            num_sum_pt_2 += gear_num_finder(i, match.span()[0])
    print("numsum: ", num_sum)
    print("numsum: ", num_sum_pt_2)


def main():
    set_schematic()
    find_part_nums()


if __name__ == "__main__":
    main()

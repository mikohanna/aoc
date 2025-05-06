#!/usr/bin/env python3
import re

DISPLAY = []

def print_display():
    print('-' * 50)
    for line in DISPLAY:
        for n in line:
            if n:
                print('@', end='')
            else:
                print(' ', end='')
        print()
    print('-' * 50)

def set_display():
    for i in range(6):
        DISPLAY.append([0] * 50)

def make_rect(width, height):
    for i in range(height):
        for j in range(width):
            DISPLAY[i][j] = 1

def rotate_row(row, pixels):
    if pixels > len(DISPLAY[row]):
        pixels %= len(DISPLAY[row])
    DISPLAY[row] = DISPLAY[row][-pixels:] + DISPLAY[row][:-pixels]

def rotate_col(col, pixels):
    if pixels > len(DISPLAY):
        pixels %= len(DISPLAY)
    extracted = []
    for row in DISPLAY:
        extracted.append(row[col])
    print(extracted)
    extracted = extracted[-pixels:] + extracted[:-pixels]
    for i, row in enumerate(DISPLAY):
        DISPLAY[i][col] = extracted[i]

def main():
    set_display()
    with open("src/day8.txt") as f:
        for line in f:
            nums = [int(n) for n in re.findall("\d+", line)]
            print(nums)
            if line.startswith("rect"):
                make_rect(nums[0], nums[1])
            if line.startswith("rotate row"):
                rotate_row(nums[0], nums[1])
            if line.startswith("rotate col"):
                rotate_col(nums[0], nums[1])
    print_display()
    print("The answer for part 1: ", sum([sum(row) for row in DISPLAY]))
    #the answer for part 2: EFEYKFRFIJ




if __name__ == "__main__":
    main()
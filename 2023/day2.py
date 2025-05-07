#!/usr/bin/env python3

import re

def main():
    sum_pt_1 = 0
    sum_pt_2 = 0
    max_red = 12
    max_green = 13
    max_blue = 14
    cntr = 1
    with open("src/day2.txt") as f:
        for line in f:
            line = line.rstrip().split(": ")[1]
            reds = max([int(n.split(" ")[0]) for n in re.findall("\d+ red", line)])
            greens = max([int(n.split(" ")[0]) for n in re.findall("\d+ green", line)])
            blues = max([int(n.split(" ")[0]) for n in re.findall("\d+ blue", line)])
            if reds <= max_red and greens <= max_green and blues <= max_blue:
                sum_pt_1 += cntr
            cntr += 1
            sum_pt_2 += reds * greens * blues
    print(sum_pt_1)
    print(sum_pt_2)
            


if __name__ == '__main__':
    main()
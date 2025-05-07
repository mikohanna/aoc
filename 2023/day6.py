#!/usr/bin/env python3

import re

# TIMES = [[7, 9], [15, 40], [30, 200]] #sample data for part 1 solution: 288
# TIMES = [[51, 377], [69, 1171], [98, 1224], [78, 1505]] #data for part 1 solution: 131376

# TIMES = [[71530, 940200]] #sample data for part 2 - solution: 71503
# TIMES_2 = [[51699878, 377117112241505]] #data for part 2 - solution: 34123437

def get_data(filename, is_part_1=True):
    with open("src/day6.txt") as f:
        if is_part_1:
            line1 = [int(n) for n in re.findall("\d+", f.readline())]
            line2 = [int(n) for n in re.findall("\d+", f.readline())]
        else:
            line1 = [int("".join(n for n in re.findall("\d+", f.readline())))]
            line2 = [int("".join(n for n in re.findall("\d+", f.readline())))]
    return list(zip(line1, line2))

#slower version
def solution_1(times):
    way_mult = 1
    for time in times:
        ways = 0
        for i in range(1, time[0]//2 + 1):
            distance = (time[0] - i) * i
            if distance > time[1]:
                ways += 1
        way_mult *= (ways * 2) if time[0] % 2 else (ways - 1) * 2 + 1
    return way_mult

#faster version
def solution_2(times):
    way_mult = 1
    for time in times:
        non_ways = 1
        for i in range(1, time[0]//2 + 1):
            distance = (time[0] - i) * i
            if distance <= time[1]:
                non_ways += 1
            else:
                break
        way_mult *= time[0] - non_ways * 2 + 1
    return way_mult
    

def main():
    TIMES = get_data("src/day6.py")
    TIMES_2 = get_data("src/day6.py", False)
    print("solution for part 1: ", solution_2(TIMES))
    print("solution for part 2: ", solution_2(TIMES_2))
            


if __name__ == "__main__":
    main()
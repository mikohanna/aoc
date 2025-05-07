#!/usr/bin/env python3

def main():
    f = open("src/day3.txt") #ord(char) - 96 and -38   
    c_sum = 0
    for l in f:
        l = l.rstrip()
        half = int(len(l) / 2)
        l1 = l[:half]
        l2 = l[half:]
        for c in l1:
            if c in l2:
                if c.islower():
                    c_sum += ord(c) - 96
                else:
                    c_sum += ord(c) - 38
                break
    print("part1: ", c_sum) #7674


    f = open("src/day3.txt") #ord(char) - 96 and -38   
    c_sum = 0
    line_group = []
    for l in f:
        l = l.rstrip()
        line_group.append(l)
        if len(line_group) == 3:
            for c in line_group[0]:
                if c in line_group[1] and c in line_group[2]:
                    if c.islower():
                        c_sum += ord(c) - 96
                    else:
                        c_sum += ord(c) - 38
                    break
            line_group = []
    print("part2: ", c_sum) #2805


main()
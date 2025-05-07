#!/usr/bin/env python3

def main():
    f = open("src/day4.txt")
    overlap_c = 0
    for l in f:
        l = l.rstrip()
        rgs = [[int(n) for n in r.split("-")] for r in l.split(",")]
        if (rgs[0][0] <= rgs[1][0] and rgs[0][1] >= rgs[1][1]) or (rgs[1][0] <= rgs[0][0] and rgs[1][1] >= rgs[0][1]):
            overlap_c += 1
    print("The answer for part 1: ", overlap_c)

    f = open("src/day4.txt")
    overlap_c = 0
    for l in f:
        l = l.rstrip()
        rgs = [[int(n) for n in r.split("-")] for r in l.split(",")]
        if (rgs[0][0] <= rgs[1][0] and rgs[0][1] >= rgs[1][0] or rgs[0][0] >= rgs[1][0] and rgs[0][0] <= rgs[1][1]):
            overlap_c += 1
    print("The answer for part 2: ", overlap_c)

main()
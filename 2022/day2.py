#!/usr/bin/env python3


def main():
    f = open("src/day2.txt") #A X - rock, B Y - paper, C Z - scissors
    my_p = 0
    for l in f:
        if l[2] == 'X':
            my_p += 1
            if l[0] == 'A':
                my_p += 3
            elif l[0] == 'B':
                my_p += 0
            elif l[0] == 'C':
                my_p += 6
        elif l[2] == 'Y':
            my_p += 2
            if l[0] == 'A':
                my_p += 6
            elif l[0] == 'B':
                my_p += 3
            elif l[0] == 'C':
                my_p += 0
        elif l[2] == 'Z':
            my_p += 3
            if l[0] == 'A':
                my_p += 0
            elif l[0] == 'B':
                my_p += 6
            elif l[0] == 'C':
                my_p += 3
    print("the answer for part 1: ", my_p) #12679

    #part2
    f = open("src/day2.txt") #A - rock, B - paper, C - scissors
    my_p = 0
    for l in f:
        if l[2] == 'X':
            my_p += 0
            if l[0] == 'A':
                my_p += 3
            elif l[0] == 'B':
                my_p += 1
            elif l[0] == 'C':
                my_p += 2
        elif l[2] == 'Y':
            my_p += 3
            if l[0] == 'A':
                my_p += 1
            elif l[0] == 'B':
                my_p += 2
            elif l[0] == 'C':
                my_p += 3
        elif l[2] == 'Z':
            my_p += 6
            if l[0] == 'A':
                my_p += 2
            elif l[0] == 'B':
                my_p += 3
            elif l[0] == 'C':
                my_p += 1
    print("the answer for part 2: ", my_p) #14470


main()
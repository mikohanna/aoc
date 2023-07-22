#!/usr/bin/env python3

#part 1:
def floor_finder(filename):
    f = open(filename)
    floor = 0
    while True:
        c = f.read(1)
        if not c:
            break
        if c == '(':
            floor += 1
        else:
            floor -= 1
    return floor


#part 2:
def basement(filename):
    f = open(filename)
    floor = 0
    position = 1
    while True:
        c = f.read(1)
        if not c:
            break
        if c == '(':
            floor += 1
        else:
            floor -= 1
            if floor == -1:
                return position
        position += 1
    return "Santa did't go to the basement"


def main():
    print("The answer for part 1: ", floor_finder("src/day1.txt")) #280
    print("The answer for part 2: ", basement("src/day1.txt")) #1797


if __name__ == "__main__":
    main()
#!/usr/bin/env python3


#part 1:
def surface(a, b, c):
    return 2*a*b + 2*a*c + 2*b*c


def wrapper_size(a, b, c):
    min_side = min(a*b, b*c, a*c)
    return min_side + surface(a, b, c)


def boxes(filename):
    f = open(filename)
    wrapping_paper = 0
    for line in f:
        sizes = [int(n) for n in line.rstrip().split("x")]
        wrapping_paper += wrapper_size(sizes[0], sizes[1], sizes[2])
    return wrapping_paper


#part 2:
def ribbon_length(a, b, c):
    return (a*b*c) + (2*a + 2*b + 2*c - 2*max(a, b, c))

def ribbons(filename):
    f = open(filename)
    ribbon = 0
    for line in f:
        sizes = [int(n) for n in line.rstrip().split("x")]
        ribbon += ribbon_length(sizes[0], sizes[1], sizes[2])
    return ribbon

def main():
    print("The answer for part 1: ", boxes("src/day2.txt")) #1588178
    print("The answer for part 2: ", ribbons("src/day2.txt")) #3783758
    


if __name__ == "__main__":
    main()
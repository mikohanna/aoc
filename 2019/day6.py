#!/usr/bin/env python3

def get_orbits(filename):
    f = open(filename)
    orbits = {}
    for line in f:
        data = line.rstrip('\n').split(")")
        orbits[data[1]] = data[0]
    return orbits


def get_checksum(filename):
    orbits = get_orbits(filename)
    checksum = 0
    for value in orbits.values():
        checksum += 1
        obj = value
        while obj != 'COM':
            checksum += 1
            obj = orbits[obj]
    return checksum


def get_santa(filename):
    orbits = get_orbits(filename)
    my_obj = orbits['YOU']
    santa_obj = orbits['SAN']
    my_orbits = []
    while my_obj != 'COM':
        my_orbits.append(orbits[my_obj])
        my_obj = orbits[my_obj]
    distance = 0
    while santa_obj not in my_orbits:
        santa_obj = orbits[santa_obj]
        distance += 1
    return len(my_orbits[:my_orbits.index(santa_obj) + 1]) + distance


def main():
    print("the answer for part 1 is: ", get_checksum("src/day6.txt")) #273985
    print("the answer for part 2 is: ", get_santa("src/day6.txt"))


main()
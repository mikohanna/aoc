#!/usr/bin/env python3

import itertools

def get_data(filename):
    f = open(filename)
    cities = {}
    for line in f:
        line = line.split()
        if line[0] not in cities:
            cities[line[0]] = {}
        if line[2] not in cities:
            cities[line[2]] = {}
        cities[line[0]][line[2]] = int(line[4])
        cities[line[2]][line[0]] = int(line[4])
    return cities


def find_min_route(cities):
    city_combo = list(itertools.permutations(cities.keys()))
    min_route = -1
    for combo in city_combo:
        route = 0
        for i in range(len(combo) - 1):
            distance = cities[combo[i]][combo[i+1]]
            if distance:
                route += distance
        if min_route == -1 or min_route > route:
            min_route = route
    return min_route


def find_max_route(cities):
    city_combo = list(itertools.permutations(cities.keys()))
    max_route = -1
    for combo in city_combo:
        route = 0
        for i in range(len(combo) - 1):
            distance = cities[combo[i]][combo[i+1]]
            if distance:
                route += distance
        if max_route == -1 or max_route < route:
            max_route = route
    return max_route




def main():
    cities = get_data("src/day9.txt")
    # part 1:
    print("The answer for part 1: ", find_min_route(cities)) #251
    # part 2:
    print("The answer for part 2: ", find_max_route(cities)) #898



if __name__ == "__main__":
    main()
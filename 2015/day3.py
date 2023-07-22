#!/usr/bin/env python3

def house_coordinates(c, house):
    if c == '<':
        house[1] -= 1
    if c == '>':
        house[1] += 1
    if c == '^':
        house[0] -= 1
    if c == 'v':
        house[0] += 1
    return house

def directions(filename):
    f = open(filename)
    houses = [] #collects coordinates of houses
    house = [0, 0] #coordinates: house[0] represents the row, house[1] the column
    while True:
        if house not in houses:
            houses.append(house[:])
        c = f.read(1)
        if not c:
            break
        house = house_coordinates(c, house)       
    return len(houses)

#part 2:
def directions_advanced(filename):
    f = open(filename)
    houses = [] #collects coordinates of houses
    house = [0, 0] #coordinates: house[0] represents the row, house[1] the column
    house_robo = [0, 0] #coordinates: house[0] represents the row, house[1] the column
    index = 0
    while True:
        if house not in houses:
            houses.append(house[:])
        if house_robo not in houses:
            houses.append(house_robo[:])
        c = f.read(1)
        if not c:
            break
        index += 1
        if index % 2:
            house = house_coordinates(c, house)
        if not index % 2:
            house_robo = house_coordinates(c, house_robo)
    return len(houses)

def main():
    print("The answer for part 1: ", directions("src/day3.txt")) #2565
    print("The answer for part 2: ", directions_advanced("src/day3.txt")) #2639

    


if __name__ == "__main__":
    main()
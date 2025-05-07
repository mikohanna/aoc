#!/usr/bin/env python3

import get_data as gd

#for part 1:
def fuel_count(crabs):
    min_fuel = sum(crabs)
    for n in range(max(crabs) + 1):
        fuel = 0 
        for crab in crabs:
            fuel += abs(n - crab)
            if fuel > min_fuel:
                break
        else:
            min_fuel = fuel
    return min_fuel

#for part 2:
def fuel_count_advanced(crabs):
    min_fuel = sum(crabs) ** 10
    for n in range(max(crabs) + 1):
        fuel = 0 
        for crab in crabs:
            fuel += (abs(n - crab) * (abs(n - crab) + 1)) // 2
            if fuel > min_fuel:
                break
        else:
            min_fuel = fuel
    return min_fuel


def main():
    crabs = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    crabs = gd.numlist_comma_sep("src/day7.txt")
    print(fuel_count(crabs)) #345035
    print(fuel_count_advanced(crabs)) #97038163


if __name__ == "__main__":
    main()
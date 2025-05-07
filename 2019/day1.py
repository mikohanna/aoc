#!/usr/bin/env python3

from get_data import get_num_list
import math

def get_fuel(mass):
    return math.floor(mass/3 - 2)

#part1:
def all_fuel(masses):
    return sum(get_fuel(n) for n in masses)

#part2:
def all_fuel2(masses):
    sum_fuel = 0
    for mass in masses:
        while mass > 0:
            mass = get_fuel(mass)
            if mass > 0:
                sum_fuel += mass
    return sum_fuel    


def main():
    nums = get_num_list("src/day1.txt")
    print("The answer for part 1: ", all_fuel(nums)) #3262356
    print("The answer for part 2: ", all_fuel2(nums)) #4890664

main()

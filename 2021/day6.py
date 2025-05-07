#!/usr/bin/env python3

import get_data as gd

#the easier, but slower way for part 1------------------------------------------------------------------

def one_day(actual_fish):
    return_fish = actual_fish[:]
    for index, fish in enumerate(return_fish):
        if fish == 0:
            return_fish[index] = 6
            return_fish.append(9)
        else:
            return_fish[index] -= 1
    return return_fish

def lanternfish(initial_fish, days):
    for i in range(days):
        initial_fish = one_day(initial_fish)
    return initial_fish

#the faster way for part 2------------------------------------------------------------------
def lantern(fish_lst, days):
    fish = [fish_lst.count(f) for f in range(10)]
    for i in range(days):
        tmp6 = fish[6]
        tmp8 = fish[8]
        fish[8] = fish[0]
        fish[6] = fish[0] + fish[7]
        for j in range(5):
            fish[j] = fish[j+1]
        fish[5] = tmp6
        fish[7] = tmp8
    return sum(fish)


def main():
    first_fish = gd.numlist_comma_sep("src/day6.txt") 
    days = 80
    fish = lantern(first_fish, days)
    print(f"After {days} days, there are {fish} lanternfish.") #380758
    days = 256
    first_fish = gd.numlist_comma_sep("src/day6.txt") 
    fish = lantern(first_fish, days)
    print(f"After {days} days, there are {fish} lanternfish.") #710623015163

if __name__ == "__main__":
    main()
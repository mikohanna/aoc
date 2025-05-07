#!/usr/bin/env python3

from get_data import get_num_list_comma_sep

#part1
def int_codes(num_list):
    nums = num_list[:]
    for i in range(0, len(nums), 4):
        if nums[i] == 1:
            nums[nums[i+3]] = nums[nums[i+1]] + nums[nums[i+2]]
        elif nums[i] == 2:
            nums[nums[i+3]] = nums[nums[i+1]] * nums[nums[i+2]]
        elif nums[i] == 99:
            break
        else:
            print("error!")
            return -1
    return nums[0]

#part2
def noun_n_verb(num_list, final_num):
    for i in range(100):
        for j in range(100):
            nums = num_list[:]
            nums[1] = i
            nums[2] = j
            if int_codes(nums) == final_num:
                return i * 100 + j


def main():
    nums = get_num_list_comma_sep("src/day2.txt")
    nums[1] = 12
    nums[2] = 2
    print("The answer for part 1: ", int_codes(nums)) #3706713
    print("The answer for part 2: ", noun_n_verb(nums, 19690720)) #8609

main()
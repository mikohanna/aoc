#!/usr/bin/env python3

import get_data as gd

def count_increase(nums):
    incr = 0
    prev = nums[0]
    for n in nums[1:]:
        if n > prev:
            incr += 1
        prev = n
    return incr

def count_increase_advanced(nums):
    incr = 0
    prev = nums[0] + nums[1] + nums[2]
    for i in range(1, len(nums) - 2):
        n = nums[i] + nums[i + 1] + nums[i + 2]
        if n > prev:
            incr += 1
        prev = n
    return incr

def main():
    nums = gd.numlist_from_file("src/day1.txt")
    print(count_increase(nums))
    print(count_increase_advanced(nums))
    


if __name__ == "__main__":
    main()

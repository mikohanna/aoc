#!/usr/bin/env python3
import re

SPELLED = "one, two, three, four, five, six, seven, eight, nine".split(', ')

def main():
    the_sum = 0
    # with open("src/day1.txt") as f:
    #     for line in f:
    #         nums = re.findall("\d", line)
    #         the_sum += int(nums[0]) * 10 + int(nums[-1])
    # print(the_sum)
    the_sum = 0
    with open("src/day1.txt") as f:
        for line in f:
            line = (line.replace("oneight", "oneeight") #TODO: replace this madness to an overlapping regex solution
                    .replace("threeight", "threeeight")
                    .replace("fiveight", "fiveeight")
                    .replace("sevenine", "sevennine")
                    .replace("eightwo", "eighttwo")
                    .replace("eighthree", "eightthree")
                    .replace("sevenine", "sevennine")
                    .replace("twone", "twoone"))
            nums = re.findall("\d|one|two|three|four|five|six|seven|eight|nine", line)
            print(nums)
            nums = [nums[0], nums[-1]]
            nums[0] = SPELLED.index(nums[0]) + 1 if len(nums[0]) > 1 else int(nums[0])
            nums[1] = SPELLED.index(nums[1]) + 1 if len(nums[1]) > 1 else int(nums[1])
            print(nums)
            the_sum += nums[0] * 10 + nums[1]
    print(the_sum)

            


if __name__ == '__main__':
    main()

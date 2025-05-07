#!/usr/bin/env python3

#part1
def is_possible_num(num):
    digits = str(num)
    is_adjacent = False
    prev_digit = digits[0]
    for digit in digits[1:]:
        if digit < prev_digit:
            return False
        if digit == prev_digit:
            is_adjacent = True
        prev_digit = digit
    return is_adjacent

#part2
def is_possible_num2(num):
    digits = str(num)
    is_adjacent = False
    adjacent_count = 0
    prev_digit = digits[0]
    for digit in digits[1:]:
        if digit < prev_digit:
            return False
        if digit == prev_digit:
            adjacent_count += 1
        else:
            if adjacent_count == 1:
                is_adjacent = True
            adjacent_count = 0
        prev_digit = digit
    if adjacent_count == 1:
        return True
    return is_adjacent


def find_passw(min_num, max_num, is_part2=False):
    if is_part2:
        return len([n for n in range(min_num, max_num + 1) if is_possible_num2(n)])
    return len([n for n in range(min_num, max_num + 1) if is_possible_num(n)])


def main():
    print("The answer for part 1: ", find_passw(248345, 746315)) #1019
    print("The answer for part 2: ", find_passw(248345, 746315, True)) #660


main()
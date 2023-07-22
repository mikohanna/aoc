#!/usr/bin/env python3
hexx = []

def str_diff_count(filename):
    with open(filename) as f:
        sum_word_diff = 0
        sum_word_diff_2 = 0
        for line in f:
            line = line.rstrip()
            sum_word_diff += word_diff(line)
            sum_word_diff_2 += word_diff(line, False)
    return (sum_word_diff, sum_word_diff_2)


def word_diff(word, is_part_1=True):
    diff = word.count('"')
    if is_part_1:
        diff += word.count('\\\\')
        for h in hexx:
            diff += word.count('\\x' + h) * 3
    else:
        diff += word.count('\\')
        diff += 2
    return diff


def main(): 
    for i in range(256):
        hexx.append(f"{i:02x}")
    ans = str_diff_count("src/day8.txt")
    print(f"The answer for part 1: {ans[0]}\nThe answer for part 2: {ans[1]}") #1350 - 2085


if __name__ == "__main__":
    main()
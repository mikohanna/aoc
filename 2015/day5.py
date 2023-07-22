#!/usr/bin/env python3

#part 1:
def is_nice(word):
    if ("ab" in word or
        "cd" in word or
        "pq" in word or
        "xy" in word):
        return False
    is_double = False
    vowel_count = 0
    for i, c in enumerate(word):
        if c in "aeiou":
            vowel_count += 1
        if i != len(word) - 1 and c == word[i+1]:
            is_double = True
        if is_double and vowel_count > 2:
            return True
    return False


def is_nice_advanced(word):
    is_twoletters = False
    is_letter_repeat = False
    for i, c in enumerate(word[:-2]):
        twoletters = c + word[i+1]
        if twoletters in word[i+2:]:
            is_twoletters = True
        if c == word[i+2]:
            is_letter_repeat = True
        if is_twoletters and is_letter_repeat:
            return True

    return False


def nice_count(filename, is_part_2=False):
    f = open(filename)
    nice = 0
    for line in f:
        if is_part_2:
            if is_nice_advanced(line):
                nice += 1
        else:
            if is_nice(line):
                nice += 1
    return nice


def main():
    print("The answer for part 1: ", nice_count("src/day5.txt"))
    print("The answer for part 2: ", nice_count("src/day5.txt", is_part_2=True))


if __name__ == "__main__":
    main()
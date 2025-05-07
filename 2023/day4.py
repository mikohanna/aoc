#!/usr/bin/env python3
import re

line_length = 193

def main():
    points = 0 #for part 1
    win_cards = [1] * line_length #for part 2
    with open("src/day4.txt") as f:
        for line in f:
            cardnum, line = line.split(":")
            cardnum = int(re.findall("\d+", cardnum)[0]) - 1
            line = line.split("|")
            win_nums, my_nums = [set([int(n) for n in re.findall("\d+", ln)]) for ln in line]
            intersec = len(win_nums.intersection(my_nums))
            points += 2 ** (intersec - 1) if intersec else 0
            for i in range( cardnum + 1, cardnum + intersec + 1):
                win_cards[i] += win_cards[cardnum]
    print("the answer for part 1: ", points)
    print("the asnwer for part 2: ", sum(win_cards))


if __name__ == "__main__":
    main()
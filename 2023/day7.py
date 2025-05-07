#!/usr/bin/env python3

CARDS = {
    "highc": [],
    "1pair": [],
    "2pair": [],
    "3kind": [],
    "fullh": [],
    "4kind": [],
    "5kind": [],
}


def set_line(card_str, is_part_2=False):
    line = []
    for i, ln in enumerate(card_str):
        if ln == 'A':
            line.append(14)
        elif ln == 'K':
            line.append(13)
        elif ln == 'Q':
            line.append(12)
        elif ln == 'J':
            if is_part_2:
                line.append(1)
            else:
                line.append(11)
        elif ln == 'T':
            line.append(10)
        else:
            line.append(int(ln))
    return line


def define_hand(line):
    card_set = set(line)
    if len(line) - len(card_set) == 4:
        return "5kind"
    if len(line) - len(card_set) == 3:
        for c in card_set:
            if line.count(c) == 4:
                return "4kind"
        return 'fullh'
    if len(line) - len(card_set) == 2:
        for c in card_set:
            if line.count(c) == 3:
                return "3kind"
        return "2pair"
    if len(line) - len(card_set) == 1:
        return "1pair"
    return "highc"


def define_hand_p2(line):
    card_set = set(line)
    if len(line) - len(card_set) == 4:
        return "5kind"
    if len(line) - len(card_set) == 3:
        if 1 in line:
            return "5kind"
        for c in card_set:
            if line.count(c) == 4:
                return "4kind"
        return 'fullh'
    if len(line) - len(card_set) == 2:
        for c in card_set:
            if line.count(c) == 3:
                return "4kind" if 1 in line else "3kind"
        if line.count(1) == 2:
            return "4kind"
        if line.count(1) == 1:
            return "fullh"
        return "2pair"
    if len(line) - len(card_set) == 1:
        return "3kind" if 1 in line else '1pair'
    return '1pair' if 1 in line else 'highc'


def set_cards(is_part_2=False):
    with open("src/day7.txt") as f:
        for line in f:
            line = line.split()
            line[1] = int(line[1])
            if is_part_2:
                line[0] = set_line(line[0], True)
                CARDS[define_hand_p2(line[0])].append(line)
            else:
                line[0] = set_line(line[0])
                CARDS[define_hand(line[0])].append(line)


def count_result():
    for card in CARDS:
        CARDS[card].sort()
    res = 0
    cntr = 1
    for v in CARDS.values():
        for e in v:
            res += cntr * e[1]
            cntr += 1
    return res


def delete_cards():
    for card in CARDS:
        CARDS[card] = []


def main():
    set_cards(False)   #for part 1    - 253910319   
    print("The answer for part 1: ", count_result())
    delete_cards()
    print(CARDS)
    set_cards(True)   #for part 2     - 254083736 
    print("The answer for part 2: ", count_result())
    

if __name__ == "__main__":
    main()
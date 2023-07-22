#!/usr/bin/env python3

import itertools

def get_data(filename):
    f = open(filename)
    persons = {}
    for line in f:
        line = line.split()
        if line[0] not in persons:
            persons[line[0]] = {}
        if line[2] == 'gain':
            persons[line[0]][line[-1][:-1]] = int(line[3])
        else:
            persons[line[0]][line[-1][:-1]] = -int(line[3])
    return persons


def table_order(persons):
    seat_combo = list(itertools.permutations(persons.keys()))
    max_happy = None
    win_combo = []                               # not part of the exercise, simply interesting
    for combo in seat_combo:
        happy = persons[combo[-1]][combo[0]]
        happy += persons[combo[0]][combo[-1]]
        for i in range(len(combo) - 1):
            happy += persons[combo[i]][combo[i+1]]
            happy += persons[combo[i+1]][combo[i]]
        if max_happy == None or max_happy < happy:
            max_happy = happy
            win_combo = combo                    # not part of the exercise, simply interesting
    print(win_combo)                             # not part of the exercise, simply interesting
    return max_happy


def include_me(persons):
    persons['me'] = {}
    for person in persons:
        persons['me'][person] = 0
        persons[person]['me'] = 0
    return persons


def main():
    # part 1:
    persons = get_data("src/day13.txt")
    print("The answer for part 1: ", table_order(persons)) # 709
    # part 2:
    persons_plus_me = include_me(persons)
    print("The answer for part 2: ", table_order(persons_plus_me)) # 668


if __name__ == "__main__":
    main()
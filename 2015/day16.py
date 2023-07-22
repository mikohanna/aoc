#!/usr/bin/env python3

AUNTS = []

SEARCHED_AUNT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

def get_data(filename):
    f = open(filename)
    for line in f:
        line = line.replace(",", "").replace(":", "").split()
        AUNTS.append({
            "index": int(line[1]),
            line[2]: int(line[3]),
            line[4]: int(line[5]),
            line[6]: int(line[7])
        })


def compare_aunt():
    possible_aunts = []
    for aunt in AUNTS:
        for k, v in aunt.items():
            if k != 'index':
                if v != SEARCHED_AUNT[k]:
                    break
        else:
            possible_aunts.append(aunt)
    return possible_aunts


#for part 2:
def compare_aunt_advanced():
    possible_aunts = []
    for aunt in AUNTS:
        for k, v in aunt.items():
            if k == 'index':
                continue
            if k == 'cats' or k == 'trees':
                if v <= SEARCHED_AUNT[k]:
                    break
            elif k == 'pomeranians' or k == 'goldfish':
                if v >= SEARCHED_AUNT[k]:
                    break
            elif v != SEARCHED_AUNT[k]:
                break
        else:
            possible_aunts.append(aunt)
    return possible_aunts


def main():
    get_data("src/day16.txt")
    possible_aunts = compare_aunt() #returns a list, just in case there are more than one that matches
    print("PART 1:")
    print(possible_aunts) #373
    print("So the answer for part 1 is: ", possible_aunts[0]['index'])
    print("PART 2:")
    possible_aunts = compare_aunt_advanced() #returns a list, just in case there are more than one that matches
    print(possible_aunts) #260
    print("So the answer for part 2 is: ", possible_aunts[0]['index'])


if __name__ == "__main__":
    main()
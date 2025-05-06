#!/usr/bin/env python3

NUMPAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

NUMPAD_2 = [
    [0, 0, 1, 0, 0],
    [0, 2, 3, 4, 0],
    [5, 6, 7, 8, 9],
    [0, 'A', 'B', 'C', 0],
    [0, 0, 'D', 0, 0]
]

def get_nums(filename):
    act_button = [1, 1] # az 5ös gomb koordinátái
    passw = []
    with open(filename) as f:
        for line in f:
            for c in line:
                if c == 'R' and act_button[1] < 2:
                    act_button[1] += 1
                if c == 'L' and act_button[1] > 0:
                    act_button[1] -= 1
                if c == 'U' and act_button[0] > 0:
                    act_button[0] -= 1
                if c == 'D' and act_button[0] < 2:
                    act_button[0] += 1
            passw.append(NUMPAD[act_button[0]][act_button[1]])
    return passw

def get_nums_2(filename):
    act_button = [2, 0] # az 5ös gomb koordinátái
    passw = []
    with open(filename) as f:
        for line in f:
            for c in line:
                # print("-> ", c, NUMPAD_2[act_button[0]][act_button[1]], " - ", act_button)
                if c == 'R' and act_button[1] < 4 and NUMPAD_2[act_button[0]][act_button[1] + 1] != 0:
                    act_button[1] += 1
                if c == 'L' and act_button[1] > 0 and NUMPAD_2[act_button[0]][act_button[1] - 1] != 0:
                    act_button[1] -= 1
                if c == 'U' and act_button[0] > 0 and NUMPAD_2[act_button[0] - 1][act_button[1]] != 0:
                    act_button[0] -= 1
                if c == 'D' and act_button[0] < 4 and NUMPAD_2[act_button[0] + 1][act_button[1]] != 0:
                    act_button[0] += 1
            # print()
            passw.append(NUMPAD_2[act_button[0]][act_button[1]])
    return passw


def main():
    print("the answer for part 1: ", "".join([str(n) for n in get_nums("src/day2.txt")]))
    print("the answer for part 2: ", "".join([str(n) for n in get_nums_2("src/day2.txt")]))


if __name__ == "__main__":
    main()
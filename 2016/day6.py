#!/usr/bin/env python3


def main():
    dict = []
    with open("src/day6.txt") as f:
        for line in f:
            line = line.strip()
            if not dict:
                for r in range(len(line)):
                    dict.append({})
            for i, c in enumerate(line):
                dict[i][c] = dict[i].get(c, 0) + 1
    ans_p1 = []
    ans_p2 = []
    for d in dict:
        d = sorted(d, key=d.get, reverse=True)
        ans_p1.append(d[0])
        ans_p2.append(d[-1])
    print("The answer for part 1: ", "".join(ans_p1))
    print("The answer for part 2: ", "".join(ans_p2))






if __name__ == "__main__":
    main()
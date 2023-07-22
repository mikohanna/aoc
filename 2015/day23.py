#!/usr/bin/env python3
from get_data import str_list_from_file

def main():
    a = 0       #you only need to change this to toggle between part 1 and part 2 (part 1: a = 0, part 2: a = 1)
    b = 0
    instructions = str_list_from_file("src/day23.txt")
    i = 0
    while i < len(instructions):
        ins = instructions[i]
        if ins.endswith("a"):
            if ins.startswith("inc"):
                a += 1
            if ins.startswith("tpl"):
                a *= 3
            if ins.startswith("hlf"):
                a /= 2
            i += 1
        elif ins.endswith("b"):
            if ins.startswith("inc"):
                b += 1
            if ins.startswith("tpl"):
                b *= 3
            if ins.startswith("hlf"):
                b /= 2
            i += 1
        else:
            details = ins.split()
            if (details[0] == "jie" and
               (details[1].startswith("a") and a % 2 != 0 or
                details[1].startswith("b") and b % 2 != 0)):
                    i += 1
                    continue
            if (details[0] == "jio" and
               (details[1].startswith("a") and a != 1 or
                details[1].startswith("b") and b != 1)):
                    i += 1
                    continue
            i += int(details[-1])
    print("a = ", a, " b = ", b) # PART 1: b=170, PART 2: b=247


if __name__ == "__main__":
    main()
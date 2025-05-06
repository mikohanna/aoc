#!/usr/bin/env python3

INSTRUCTIONS = []
VALUES = {}

def one_step(index):
    if index >= len(INSTRUCTIONS):
        return
    ins = INSTRUCTIONS[index]
    if ins[0] == 'cpy':
        if ins[1].isdigit():
            VALUES[ins[2]] = int(ins[1])
        else:
            VALUES[ins[2]] = VALUES[ins[1]]
    elif ins[0] == 'inc':
        VALUES[ins[1]] += 1
    elif ins[0] == 'dec':
        VALUES[ins[1]] -= 1
    elif ins[0] == 'jnz':
        if ins[1] != 0:
            one_step(index + int(ins[2]))
    one_step(index + 1)  

def main():
    with open("src/day12.txt") as f:
        for ins in f:
            INSTRUCTIONS.append(ins.split())
    # one_step(0)
    index = 0
    VALUES['c'] = 1
    # for i in range(300):
    while index < len(INSTRUCTIONS):
        ins = INSTRUCTIONS[index]
        if ins[0] == 'cpy':
            if ins[1].isdigit():
                VALUES[ins[2]] = int(ins[1])
            else:
                VALUES[ins[2]] = VALUES[ins[1]]
        elif ins[0] == 'inc':
            VALUES[ins[1]] += 1
        elif ins[0] == 'dec':
            VALUES[ins[1]] -= 1
        elif ins[0] == 'jnz':
            if ins[1].isdigit() and ins[1] != 0 or ins[1] in VALUES and VALUES[ins[1]] != 0:
                index += int(ins[2])
                continue
        index += 1

    print(VALUES)
            


if __name__ == "__main__":
    main()
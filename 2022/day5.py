#!/usr/bin/env python3

stacks = [
    ["R","P","C","D","B","G"],
    ["H","V","G"],
    ["N","S","Q","D","J","P","M"],
    ["P","S","L","G","D","C","N","M"],
    ["J","B","N","C","P","F","L","S"],
    ["Q","B","D","Z","V","G","T","S"],
    ["B","Z","M","H","F","T","Q"],
    ["C","M","D","B","F"],
    ["F","C","Q","G"],
]

def move_stack(quant, src, dest):
    for e in (stacks[src][-quant:]): #this is for part2! Use this line for the result of part2
    # for e in reversed(stacks[src][-quant:]): #this is for part1! Use this line for the result of part1
        stacks[dest].append(e)
    del stacks[src][-quant:]


def get_message():
    for stack in stacks:
        print(stack[-1], end="")
    print()


def main():
    f = open("src/day5.txt")
    for i, l in enumerate(f):
        l = l.rstrip()
        if i > 9:
            l = l.split()
            move_stack(int(l[1]), int(l[3]) - 1, int(l[5]) - 1)
    get_message()


main()
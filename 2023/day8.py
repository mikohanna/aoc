#!/usr/bin/env python3
import re

INSTRUCTIONS = []
NODE_MAP = {}


def set_data(filename):
    global INSTRUCTIONS
    with open(filename) as f:
        INSTRUCTIONS = [0 if n == 'L' else 1 for n in f.readline().strip()]
        for line in f:
            line = (re.findall('\w+', line))
            if line:
                NODE_MAP[line[0]] = (line[1], line[2])

#part 1:
def find_ZZZ():
    act_node = 'AAA'
    steps = 0
    index = 0
    while act_node != 'ZZZ':
        act_node = NODE_MAP[act_node][INSTRUCTIONS[index]]
        steps += 1
        index += 1
        if index == len(INSTRUCTIONS):
            index = 0
    return steps

#part 2:
def find_starter_points():
    starter_points = []
    for key in NODE_MAP.keys():
        if key[-1] == 'A':
            starter_points.append(key)
    return starter_points


def find_z_end_steps():
    act_nodes = find_starter_points()
    z_end_steps = []
    for node in act_nodes:
        index = 0
        steps = 0
        while node[-1] != 'Z':
            node = NODE_MAP[node][INSTRUCTIONS[index]]
            steps += 1
            index += 1
            if index == len(INSTRUCTIONS):
                index = 0
        z_end_steps.append(steps)
    return z_end_steps


def lcm(num1, num2):       #least common multiple
    mx = max([num1, num2])
    n = mx
    while True:
        if n % num1 == 0 and n % num2 == 0:
            return n
        n += mx


def find_xxZ():
    z_steps = find_z_end_steps()  #how many steps you can find the z-ended node
    while len(z_steps) > 1:
        new_list = []
        for i in range(len(z_steps) // 2):
            new_list.append(lcm(z_steps[i], z_steps[-(i + 1)]))
        if len(z_steps) % 2:
            new_list.append(z_steps[len(z_steps) // 2])
        z_steps = new_list
    return z_steps[0]
        

def main():
    set_data("src/day8.txt")
    print("the answer for part 1: ", find_ZZZ())
    print("the answer for part 2: ", find_xxZ())



if __name__ == "__main__":
    main()
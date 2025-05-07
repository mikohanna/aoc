#!/usr/bin/env python3

import get_data as gd

def forward_depth_measure(data):
    forward = 0
    depth = 0
    for d in data:
        if d[0] == 'forward':
            forward += d[1]
        elif d[0] == 'down':
            depth += d[1]
        elif d[0] == 'up':
            depth -= d[1]
        else:
            return 'Invalid input!'
    return forward * depth


def forward_depth_measure_advanced(data):
    forward = 0
    aim = 0
    depth = 0
    for d in data:
        if d[0] == 'forward':
            forward += d[1]
            depth += d[1] * aim
        elif d[0] == 'down':
            aim += d[1]
        elif d[0] == 'up':
            aim -= d[1]
        else:
            return 'Invalid input!'
    return forward * depth



def main():
    d = gd.str_n_num_list_from_file("src/day2.txt")
    #d = [['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]
    print(forward_depth_measure(d))
    print(forward_depth_measure_advanced(d))


if __name__ == "__main__":
    main()
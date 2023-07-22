#!/usr/bin/env python3
import json

def find_num(elements, num_sum=0):
    if type(elements) == dict:
        for v in elements.values():
            if type(v) == int or type(v) == float:
                num_sum += v
            elif type(v) != str:
                num_sum = find_num(v, num_sum)
    if type(elements) == list:
        for v in elements:
            if type(v) == int or type(v) == float:
                num_sum += v
            elif type(v) != str:
                num_sum = find_num(v, num_sum)
    return num_sum


def find_num_advanced(elements, num_sum=0):
    if type(elements) == dict:
        values = elements.values()
        if "red" not in values:
            for v in elements.values():
                if type(v) == int or type(v) == float:
                    num_sum += v
                elif type(v) != str:
                    num_sum = find_num_advanced(v, num_sum)
    if type(elements) == list:
        for v in elements:
            if type(v) == int or type(v) == float:
                num_sum += v
            elif type(v) != str:
                num_sum = find_num_advanced(v, num_sum)
    return num_sum



def main():
    f = open("src/day12.json")
    d = json.load(f)
    print("The answer for part 1: ", find_num(d)) # 111754
    print("The answer for part 2: ", find_num_advanced(d)) # 65402



if __name__ == "__main__":
    main()
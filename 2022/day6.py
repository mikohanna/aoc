#!/usr/bin/env python3

def is_individual(chrs):
    wrd = []
    for c in chrs:
        if c in wrd:
            return False
        else:
            wrd.append(c)
    return True

def main():
    src = open("src/day6.txt").read()
    segment = []
    num = 4
    num = 14 #comment this out if you want the result for part 1, stay this line if you want the result for part 2
    for i in range(len(src) - num):
        segment = src[i:i+num]
        if is_individual(segment):
            print("the answer: ", i + num)
            break



main()
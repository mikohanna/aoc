#!/usr/bin/env python3

import get_data as gd
import math


def top_calorie_finder(fn):
    f= open(fn)
    calSum = 0
    max_cal = 0
    sec = -1
    th = -2
    for l in f:
        l = l.rstrip()
        if not len(l):
            if calSum > max_cal:
                max_cal = calSum
            calSum = 0
        else:
            calSum += int(l)
    return max_cal + sec + th


def top_3_calorie_finder(fn):
    f= open(fn)
    calSum = 0
    cals = []
    for l in f:
        l = l.rstrip()
        if not len(l):
            cals.append(calSum)
            calSum = 0
        else:
            calSum += int(l)
    s = sorted(cals)
    return s[-1] + s[-2] + s[-3]


def main():
    print("the answer for part 1: ", top_calorie_finder("src/day1.txt")) #69307
    print("the answer for part 2: ", top_3_calorie_finder("src/day1.txt")) #206104
main()

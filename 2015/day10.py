#!/usr/bin/env python3

from unicodedata import digit


def one_round(digits):
    res = []
    cnt = 1
    for i, d in enumerate(digits[:-1]):
        if d == digits[i + 1]:
            cnt += 1
        else:
            res.append(cnt)
            res.append(d)
            cnt = 1
    res.append(cnt)
    res.append(digits[-1])
    return res

def num_to_lst(num):
    return [int(n) for n in str(num)]

def look_n_say(num, rounds):
    digits = num_to_lst(num)
    for _ in range(rounds):
        digits = one_round(digits)
    return digits


def main():
    #part 1:
    result = look_n_say(1321131112, 40)
    print("The answer for part 1: ", len(result)) #492982
    #part 2:
    result2 = look_n_say(1321131112, 50)
    print("The answer for part 2: ", len(result2)) #6989950


if __name__ == "__main__":
    main()
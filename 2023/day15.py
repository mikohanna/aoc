#!/usr/bin/env python3

def hash_alg(word):
    val = 0
    for c in word:
        val += ord(c)
        val *= 17
        val %= 256
    return val

def set_boxes(sequence):
    boxes = {}
    for s in sequence:
        if '=' in s:
            label, focal = s.split('=')
            h = hash_alg(label)
            if h not in boxes:
                boxes[h] = {}
            boxes[h][label] = focal
        else:
            label = s[:-1]
            h = hash_alg(label)
            if h in boxes and label in boxes[h]:
                del boxes[h][label]
    return boxes


def main():
    sequence = open("src/day15.txt").readline().split(",")
    res = 0
    for s in sequence:
        res += hash_alg(s)
    print("the answer for part 1: ", res)

    boxes = set_boxes(sequence)
    power = 0
    for key, lenses in boxes.items():
        for i, focal in enumerate(lenses.values()):
            power += (key+1) * (i+1) * int(focal)
    print("the answer for part 2: ", power)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3

def main():
    src = open("src/day10.txt").read().split()
    #PART 1:
    x = 1
    checkpoint = 20
    sum_x = 0
    for i, ins in enumerate(src):
        if i == checkpoint - 1:
            sum_x += x * (i+1)
            checkpoint += 40
        if ins.isdigit() or ins.startswith('-'):
            x += int(ins)
    print("the answer for part 1: ", sum_x)

    #PART 2:
    print("part 2:")
    pixels = []
    pixel_index = 0
    x = 1
    for i, ins in enumerate(src):
        if pixel_index <= x+1 and pixel_index >= x-1:
            pixels.append('#')
        else:
            pixels.append(' ')
        pixel_index += 1
        if pixel_index == 40:
            pixels.append('\n')
            pixel_index = 0
        if ins.isdigit() or ins.startswith('-'):
            x += int(ins)
    print("".join(pixels))
    


if __name__ == '__main__':
    main()
#!/usr/bin/env python3

import enum
from PIL import Image

def get_layers(filename, width, height):
    data = open(filename).read().rstrip('\n')
    layers = []
    layer = []
    one_row = []
    row_count = 0
    col_count = 0
    for c in data:
        one_row.append(c)
        col_count += 1
        if col_count == width:
            col_count = 0
            layer.append(one_row)
            one_row = []
            row_count += 1
        if row_count == height:
            layers.append(layer)
            layer = []
            row_count = 0
    return layers

#part1:
def occurence(layer, what):
    return sum([row.count(what) for row in layer])

#part1:
def find_layer(layers):
    chosen_layer = []
    min_zeros = len(layers[0]) * len(layers[0][0])
    for layer in layers:
        zeros = occurence(layer, '0')
        if zeros < min_zeros:
            min_zeros = zeros
            chosen_layer = layer
    return occurence(chosen_layer, '1') * occurence(chosen_layer, '2')


#part2:
def decoder(layers):
    img = [['5'] * len(layers[0][0]) for _ in range(len(layers[0]))]
    for layer in layers:
        for i, row in enumerate(layer):
            for j, val in enumerate(row):
                if img[i][j] == '5' and val != '2':
                    img[i][j] = val
    return img

def pretty_print(matrix):
    for row in matrix:
        for val in row:
            print(val, end=" ")
        print()


def main():
    width = 25
    height = 6
    layers = get_layers("src/day8.txt", width, height)
    print("The answer for part 1: ", find_layer(layers)) #1690
    src = decoder(layers)
    binaryData = [255 if c == '1' else 0 for row in src for c in row]
    picture = Image.new(mode="L", size=(width, height))
    picture.putdata(binaryData)
    picture.save("passw_for_day8.pbm")

main()
#!/usr/bin/env python3

import get_data as gd


def get_gamma(data):
    zero_count = [0] * len(data[0])
    for d in data:
        for n in range(len(d)):
            if d[n] == '0':
                zero_count[n] += 1
    binary_stuff = []
    for z in zero_count:
        if z > len(data)/2:
            binary_stuff.append('0')
        else:
            binary_stuff.append('1')
    return ''.join(binary_stuff)

def get_epsilon(gamma):
    epsilon = []
    for c in gamma:
        if c == '0':
            epsilon.append('1')
        else:
            epsilon.append('0')
    return ''.join(epsilon)


def get_consumption(data):
    gamma = get_gamma(data)
    epsilon = get_epsilon(gamma)
    return int(gamma, 2) * int(epsilon, 2)

def get_oxygen_generator_ratingg(data):
    zero_count = 0
    remains = []
    for i in range(len(data[0])):
        for b in data:
            if b == '0':
                zero_count += 1
        common = '1'
        if zero_count > len(data)/2:
            common = '0'
        remains = []
        for b in data:
            if data[i] == common:
                remains.append(data[i])
        if len(remains) < 2:
            break
        data = remains[:]
    return data

def zero_counter(data, index):
    zero_count = 0
    for d in data:
        if d[index] == '0':
            zero_count += 1 
    return zero_count


def get_generator_rating(data, is_oxigen=True): #if is_oxigen is False, then is counts the CO2 scrubber rating
    remain = data[:]
    index = 0
    while len(remain) > 1:
        zeros = zero_counter(remain, index)
        common = '1'
        if zeros > len(remain)/2:
            common = '0'
        if is_oxigen:
            remain = [n for n in remain if n[index] == common]
        else:
            remain = [n for n in remain if n[index] != common]
        index += 1
    return "".join(remain)

def get_life_support_rating(data):
    return int(get_generator_rating(data), 2) * int(get_generator_rating(data, False), 2)


def main():
    d = gd.str_list_from_file("src/day3.txt")
    #d = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    print(get_consumption(d))
    print(get_life_support_rating(d))
    


if __name__ == "__main__":
    main()
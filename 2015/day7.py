#!/usr/bin/env python3

VALUES = {}

def turn_digit(data):
    if type(data) == int:
        return data
    if type(data) == str and data.isdigit():
        return int(data)


def simple_operation(value):
    if type(turn_digit(value)) == int:
        return turn_digit(value)
    if value in VALUES and type(turn_digit(VALUES[value])) == int:
            return turn_digit(VALUES[value])
    return [value]


def not_operation(value):
    if type(turn_digit(value)) == int:
        return ~(turn_digit(value)) & 0xFFFF
    if value in VALUES and type(turn_digit(VALUES[value])) == int:
        return ~(turn_digit(VALUES[value])) & 0xFFFF
    return ["NOT", value]


def other_operation(op1, op2, operator):
    if type(turn_digit(op1)) == int:
        op1 = turn_digit(op1)
    if type(turn_digit(op2)) == int:
        op2 = turn_digit(op2)
    if op1 in VALUES and type(turn_digit(VALUES[op1])) == int:
        op1 = turn_digit(VALUES[op1])
    if op2 in VALUES and type(turn_digit(VALUES[op2])) == int:
        op2 = turn_digit(VALUES[op2])
    if type(op1) == int and type(op2) == int:
        if operator == "AND":
            return op1 & op2
        if operator == "OR":
            return op1 | op2
        if operator == "RSHIFT":
            return op1 >> op2
        if operator == "LSHIFT":
            return op1 << op2
    return [op1, operator, op2]


def handle_one_line(line_data):
    if len(line_data) == 1:
        return simple_operation(line_data[0])
    if line_data[0] == "NOT":
        return not_operation(line_data[1])
    else:
        return other_operation(line_data[0], line_data[2], line_data[1])


def data_from_file(filename):
    f = open(filename)
    for line in f:
        line_data = line.split()
        VALUES[line_data[-1]] = line_data[:-2] #levágjuk a végéről a nyilacskát és az eredményt, ami a dictionary kulcsa


def operations():
    while(not is_values_only_nums(VALUES)):
        for k, v in VALUES.items():
            if type(v) == list:
                VALUES[k] = handle_one_line(v)


def print_dict(dict):                 #It's made for only if you want to see the rest of the values.
    for k, v in dict.items():
        print(f"{k}: {v}")


def is_values_only_nums(dict):
    for v in dict.values():
        if type(v) != int:
            return False
    return True


def solver_1(is_part_2=False):
    data_from_file("src/day7.txt")
    if is_part_2:
        operations() 
    else:
        operations()  


def solver_2(value_of_a):
    VALUES = {}
    operations()


def main():
    #part 1:
    data_from_file("src/day7.txt")
    operations()
    a_value = VALUES['a']
    print('Part 1:\nThe value of "a" is: ', a_value) #956
    #part 2:
    data_from_file("src/day7.txt")
    VALUES['b'] = a_value
    operations()
    print('Part 2:\nThe value of "a" is: ', VALUES['a']) #40149



if __name__ == "__main__":
    main()
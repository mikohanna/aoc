def numlist(filename): 
    #input: one number per line data
    # output: list of integers
    f = open(filename)
    numlist = []
    for line in f:
        numlist.append(int(line.rstrip()))
    return numlist


def numlist_comma_sep(filename):
    #input: one line, comma separated list of nubers
    # output: list of integers
    f = open(filename)
    d = f.read()
    return [int(n) for n in d.split(",")]

#for day2
def str_n_num_list(filename):
    #returns a list of str-int mix list (first element is a string, the second is an int)
    f = open(filename)
    numlist = []
    for line in f:
        oneline_data = line.rstrip('\n').split(' ')
        oneline_data[1] = int(oneline_data[1])
        numlist.append(oneline_data)
    return numlist


def str_list(filename):
    #input: lines of string
    #output: list of strings
    f = open(filename)
    strlist = []
    for line in f:
        strlist.append(line.rstrip('\n'))
    return strlist

def numlist_list_from_str_list(filename):
    str_list = str_list(filename)
    num_list = []
    for s in str_list:
        num_list.append([int(n) for n in s])
    return num_list
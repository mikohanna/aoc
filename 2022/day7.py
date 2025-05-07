#!/usr/bin/env python3

from get_data import str_list

dirs = {}

def sizing(dir_name):
    for child in dirs[dir_name]['children']:
        if not dirs[child]['children']:
            dirs[dir_name]['size'] += dirs[child]['size']
            dirs[dir_name]['children'].remove(child)
        else:
            sizing(child)

def main():
    src = str_list("src/day7.txt")
    src = [s.split() for s in src]
    act_dir = []
    for l in src:
        if l[-1] == 'ls':
            continue
        if l[1] == 'cd':
            if l[2] != '..':
                act_dir.append(l[2])
                dirs["/".join(act_dir)] = {"size" : 0, "children" : []}
            else:
                del act_dir[-1]
        elif l[0] == 'dir':
            dirs["/".join(act_dir)]['children'].append("/".join(act_dir) + "/" + l[1])
        else:
            dirs["/".join(act_dir)]['size'] += int(l[0])
    for dir in dirs:
        while dirs[dir]['children']:
            sizing(dir)
    cnt = 0
    for dir in dirs:
        size = dirs[dir]['size']
        if size <= 100000:
            cnt += size
    print("answer for part 1: ", cnt) #1582412

    #part2
    total = 40000000
    needed_size = dirs['/']['size'] - total
    sizes = []
    for dir in dirs:
        sizes.append(dirs[dir]['size'])
    sizes.sort()
    for n in sizes:
        if n > needed_size: 
            print("answer for part 2: ", n)
            break

main()
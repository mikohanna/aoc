#!/usr/bin/env python3

num_grid = []


def get_num_grid(fname):
    f = open(fname)
    for l in f:
        ln = [int(c) for c in l.rstrip()]
        num_grid.append(ln)


def check_visibility(index):
    is_visible = [True, True, True, True] #0: egy sor balról / 1: egy sor jobbról / 2: egy oszlop fentről / 3: egy oszlop lentről
    num = num_grid[index[0]][index[1]]
    for n in num_grid[index[0]][:index[1]]:
        if n >= num:
            is_visible[0] = False
            break
    for n in num_grid[index[0]][index[1]+1:]:
        if n >= num:
            is_visible[1] = False
            break
    for ln in num_grid[:index[0]]:
        if ln[index[1]] >= num:
            is_visible[2] = False
            break
    for ln in num_grid[index[0]+1:]:
        if ln[index[1]] >= num:
            is_visible[3] = False
            break
    return is_visible


def check_visibility2(index):
    is_visible = [0, 0, 0, 0] #0: egy sor balról / 1: egy sor jobbról / 2: egy oszlop fentről / 3: egy oszlop lentről
    num = num_grid[index[0]][index[1]]
    for n in reversed(num_grid[index[0]][:index[1]]):
        is_visible[0] += 1
        if n >= num:
            break
    for n in num_grid[index[0]][index[1]+1:]:
        is_visible[1] += 1
        if n >= num:
            break
    for ln in reversed(num_grid[:index[0]]):
        is_visible[2] += 1
        if ln[index[1]] >= num:
            break
    for ln in num_grid[index[0]+1:]:
        is_visible[3] += 1
        if ln[index[1]] >= num:
            break
    return is_visible[0] * is_visible[1] * is_visible[2] * is_visible[3]


def cnt_vis():
    edge = len(num_grid) * 2 + len(num_grid[0]) * 2 - 4
    vis_trees = 0
    for i in range(1,len(num_grid)-1):
        for j in range(1,len(num_grid[0])-1):
            truf = check_visibility([i,j])
            if  truf[0] or truf[1] or truf[2] or truf[3]:
                vis_trees += 1
    print(vis_trees + edge)


def cnt_vis2():
    max_scope = 0
    for i in range(1,len(num_grid)-1):
        for j in range(1,len(num_grid[0])-1):
            truf = check_visibility2([i,j])
            if truf > max_scope:
                max_scope = truf
    print(max_scope)


def main():
    get_num_grid("src/day8.txt")
    print("answer for part 1: ", end="")
    cnt_vis() #1679
    print("answer for part 2: ", end="")
    cnt_vis2() #536625
    

main()
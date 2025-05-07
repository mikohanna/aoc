#!/usr/bin/env python3

def get_surface(coords):
    side_cnt = 0
    for x1, y1, z1 in coords:
        for x2, y2, z2 in coords:
            if abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2) == 1:
                side_cnt += 1
    return len(coords) * 6 - side_cnt

def get_minmax_coords(coords):
    min_coords = [1000, 1000, 1000]
    max_coords = [0, 0, 0]
    for x, y, z in coords:
        if x > max_coords[0]:
            max_coords[0] = x
        if x < min_coords[0]:
            min_coords[0] = x
        if y > max_coords[1]:
            max_coords[1] = y
        if y < min_coords[1]:
            min_coords[1] = y
        if z > max_coords[2]:
            max_coords[2] = z
        if z < min_coords[2]:
            min_coords[2] = z
    return min_coords + max_coords

def get_bubbles(coords):
    x_min, y_min, z_min, x_max, y_max, z_max = get_minmax_coords(coords)
    air_coords = []
    for i in range(x_min + 1, x_max):
        for j in range(y_min + 1, y_max):
            for k in range(z_min + 1, z_max):
                crd = [i, j, k]
                if crd in coords:
                    continue
                is_blocked = 0
                for xx in range(crd[0] + 1, x_max + 1):
                    if [xx, crd[1], crd[2]] in coords:
                        is_blocked += 1
                        break
                for xx in reversed(range(x_min, crd[0])):
                    if [xx, crd[1], crd[2]] in coords:
                        is_blocked += 1
                        break
                for yy in range(crd[1] + 1, y_max + 1):
                    if [crd[0], yy, crd[2]] in coords:
                        is_blocked += 1
                        break
                for yy in reversed(range(y_min, crd[1])):
                    if [crd[0], yy, crd[2]] in coords:
                        is_blocked += 1
                        break
                for zz in range(crd[2] + 1, z_max + 1):
                    if [crd[0], crd[1], zz] in coords:
                        is_blocked += 1
                        break
                for zz in reversed(range(z_min, crd[2])):
                    if [crd[0], crd[1], zz] in coords:
                        is_blocked += 1
                        break
                if is_blocked == 6:
                    air_coords.append(crd)
    return air_coords

def correct_air_coords(air_coords, coords):
    air_crds = air_coords[:]
    x_min, y_min, z_min, x_max, y_max, z_max = get_minmax_coords(air_coords)
    is_removed = False
    for crd in air_coords:
        for xx in range(crd[0] + 1, x_max + 1):
            moved_crd = [xx, crd[1], crd[2]]
            if moved_crd not in coords and moved_crd not in air_coords:
                air_crds.remove(crd)
                is_removed = True
                break
            if moved_crd in coords:
                break
        if is_removed:
            continue
        for xx in reversed(range(x_min, crd[0])):
            moved_crd = [xx, crd[1], crd[2]]
            if moved_crd not in coords and moved_crd not in air_coords:
                air_crds.remove(crd)
                is_removed = True
                break
            if moved_crd in coords:
                break
        if is_removed:
            continue
        for yy in range(crd[1] + 1, y_max + 1):
            moved_crd = [crd[0], yy, crd[2]]
            if moved_crd not in coords and moved_crd not in air_coords:
                air_crds.remove(crd)
                is_removed = True
                break
            if moved_crd in coords:
                break
        if is_removed:
            continue
        for yy in reversed(range(y_min, crd[1])):
            moved_crd = [crd[0], yy, crd[2]]
            if moved_crd not in coords and moved_crd not in air_coords:
                air_crds.remove(crd)
                is_removed = True
                break
            if moved_crd in coords:
                break
        if is_removed:
            continue
        for zz in range(crd[2] + 1, z_max + 1):
            moved_crd = [crd[0], crd[1], zz]
            if moved_crd not in coords and moved_crd not in air_coords:
                air_crds.remove(crd)
                is_removed = True
                break
            if moved_crd in coords:
                break
        if is_removed:
            continue
        for zz in reversed(range(z_min, crd[2])):
            moved_crd = [crd[0], crd[1], zz]
            if moved_crd not in coords and moved_crd not in air_coords:
                air_crds.remove(crd)
                is_removed = True
                break
            if moved_crd in coords:
                break
    return air_crds

def main():
    coords = []
    with open("src/day18.txt") as f: # 6 1 
        for l in f:
            coords.append([int(n) for n in l.split(',')])
    surface = get_surface(coords) #4288
    air_coords = get_bubbles(coords)
    prev_len = -1
    while len(air_coords) != prev_len:
        prev_len = len(air_coords)
        air_coords = correct_air_coords(air_coords, coords)

    air = get_surface(air_coords)
    print("answer for part 1: ", surface) #4288
    print("air: ", air)
    print("answer for part 2: ", surface - air) #2494

main()
    
    
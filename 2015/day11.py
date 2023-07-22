#!/usr/bin/env python3

def is_increasing(passw):
    for i, c in enumerate(passw[:-2]):
        if ord(c) == ord(passw[i+1]) - 1 and ord(c) == ord(passw[i+2]) - 2:
            return True
    return False


def not_contain(passw):
    return not ('o' in passw or'i' in passw or 'l' in passw)


def double_char(passw):
    cnt = 0
    index_double = 0
    for i, c in enumerate(passw[:-1]):
        if c == passw[i+1] and i != index_double + 1:
            cnt += 1
            index_double = i
            if cnt == 2:
                return True
    return False


def is_valid(passw):
    return not_contain(passw) and double_char(passw) and is_increasing(passw)

def one_step(passw):
    if passw[-1] != 'z':
        incr_char = chr(ord(passw[-1]) + 1)
        return passw[:-1] + incr_char
    cnt = 2
    for c in reversed(passw[:-1]):
        if c == 'z':
            cnt += 1
        else: 
            break
    incr_char = chr(ord(passw[-cnt]) + 1)
    return passw[:-cnt] + incr_char + 'a'*(cnt-1)
    
def find_passw(first_passw):
    passw = first_passw[:]
    while(not is_valid(passw)):
        passw = one_step(passw)
    return passw


def main():
    #part 1:
    new_passw = find_passw("hxbxwxba")
    print("The answer for part 1: ", new_passw) #hxbxxyzz
    #part 2:
    new_passw_2 = one_step(new_passw)
    print("The answer for part 2: ", find_passw(new_passw_2)) #hxcaabcc


if __name__ == "__main__":
    main()
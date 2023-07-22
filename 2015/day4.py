#!/usr/bin/env python3

import hashlib

def find_lowest_num(sk, zeros):
    num = 0
    hashed_key = ""
    while not hashed_key.startswith("0" * zeros):
        hashed_key = str(hashlib.md5((sk + str(num)).encode()).hexdigest())
        num += 1
    return num - 1



def main():
    print("The answer for part 1: ", find_lowest_num("ckczppom", 5)) # 117946
    print("The answer for part 2: ", find_lowest_num("ckczppom", 6)) # 3938038


if __name__ == "__main__":
    main()
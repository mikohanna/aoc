#!/usr/bin/env python3
import re

def is_room(name, chx):
    letters = {}
    for c in name:
        letters[c] = letters.get(c, 0) + 1
    letters = dict(sorted(letters.items()))
    k_sorted = sorted(letters, key=letters.get, reverse=True)
    return k_sorted[:5] == list(chx)

def decrypt(word, num):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    num %= len(abc)
    ans = []
    for c in word:
        idx = abc.index(c) + num
        if idx >= len(abc):
            idx -= len(abc)
        ans.append(abc[idx])
    return "".join(ans)

def main():
    s = 'aczupnetwp-mfyyj-opalcexpye-'
    print(decrypt('aczupnetwp', 977))

    sector_sum = 0
    with open('src/day4.txt') as f:
        for ln in f:
            enc_name, checksum = re.findall('\D+', ln)
            if is_room(enc_name.replace('-', ''), checksum[1:6]):
                sector = int(re.findall('\d+', ln)[0])
                sector_sum += sector
                name = []
                name_words = enc_name[:-1].split("-")
                for word in name_words:
                    name.append(decrypt(word, sector))
                name = " ".join(name)
                #these names are awesome :)
                # print(name)
                if "north" in name:
                    print("The answer for part 2: '", name, "' sector ID: ", sector)
        print("The answer for part 1: ", sector_sum)


if __name__ == "__main__":
    main()
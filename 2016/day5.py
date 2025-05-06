#!/usr/bin/env python3
import hashlib

def main():
    input = 'ojvtpuvg'
    i = 0
    counter_p1 = 0
    counter_p2 = 0
    passw_len = 8
    passw_p1 = []
    passw_p2 = ['_'] * passw_len
    while counter_p2 < passw_len:
        s = hashlib.md5((input + str(i)).encode()).hexdigest()
        i += 1
        if s.startswith('00000'):
            passw_p1.append(s[5])
            counter_p1 += 1
            if s[5].isdigit() and int(s[5]) < passw_len and passw_p2[int(s[5])] == '_':
                passw_p2[int(s[5])] = s[6]
                counter_p2 += 1
        if counter_p1 == passw_len:
            print("The answer for part 1:", "".join(passw_p1))
            counter_p1 += 1
    print("The answer for part 2:", "".join(passw_p2))


if __name__ == "__main__":
    main()
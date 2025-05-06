#!/usr/bin/env python3

def find_abba(word):
    for i, c in enumerate(word[:-3]):
        if c == word[i + 3] and word[i + 1] == word[i + 2] and c != word[i + 1]:
            return True
    return False

def get_bab(word): #finds all aba pattern in the word, make the bab pattern and returns it in a list
    babs = []
    for i, c in enumerate(word[:-2]):
        if c == word[i + 2] and c != word[i + 1]:
            babs.append(word[i+1] + c + word[i+1])
    return babs

def main():
    # print(get_bab("zazbzcwbcac"))
    tls_supported = 0
    ssl_supported = 0
    with open("src/day7.txt") as f:
        for line in f:
            ip_parts = line.strip().replace("[", "-").replace("]", "-").split("-")
            is_tls_supported = False
            babs = []
            hyper = []
            for i, ip in enumerate(ip_parts): # for part 1
                if find_abba(ip):
                    if i % 2 != 0:
                        is_tls_supported = False
                        break
                    is_tls_supported = True
            for i, ip in enumerate(ip_parts): # for part 2
                if i % 2 == 0:
                    babz = get_bab(ip)
                    if babz:
                        for bab in babz:
                            babs.append(bab)
                else:
                    hyper.append(ip)
            tls_supported += 1 if is_tls_supported else 0
            is_ssl_supported = False
            if babs:
                for h in hyper:
                    for bab in babs:
                        if bab in h:
                            is_ssl_supported = True
                            break
                    if is_ssl_supported:
                        ssl_supported += 1
                        break

    print("The answer or part 1: ", tls_supported)
    print("The answer or part 2: ", ssl_supported)


if __name__ == "__main__":
    main()
# Created by JiaYi Lim on 13/1/2014

import sys

def string_list(n, string):
    letters = set(list(string))
    perms = permute(n, letters)
    return ','.join(sorted(perms))

def permute(n, letters, current=''):
    results = set()
    if len(current) == n-1:
        return set(letters)
    for c in letters:
        variants = permute(n, letters, current+c)
        for v in variants:
            results.add(c+v)
    return results

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line != '':
                n, string = line.split(',')
                print string_list(int(n), string)


if __name__ == '__main__':
    start()
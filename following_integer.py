# Created by JiaYi Lim on 13/1/2014

import sys

def permute(string, current=''):
    if len(string) == 1:
        return set(string)
    perms = set()
    for i, c in enumerate(string):
        variants = permute(string[:i]+string[i+1:], current+c)
        for v in variants:
            perms.add(c+v)
    return perms

def find_next(string, num=''):
    if not num:
        num = int(string)
    perms = sorted([ int(p) for p in permute(string) ])
    for i in range(len(perms)-1):
        if perms[i] == num:
            return perms[i+1]
    # num is the last permutation
    string += '0'
    return find_next(string, num)

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            print find_next(line)


if __name__ == '__main__':
    start()
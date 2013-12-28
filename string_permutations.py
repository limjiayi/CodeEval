# Created by JiaYi Lim on 26/12/2013

import sys

def permute(string, current=''):
    if len(string) == 1:
        return [string]
    perms = []
    for i in range(len(string)):
        char = string[i]
        remainder = string[:i] + string[i+1:]
        variants = permute(remainder, current+char)
        for variant in variants:
            perms.append(char+variant)
    return perms

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            perms = permute(line)
            perms = ','.join(sorted(perms))
            print perms

if __name__ == '__main__':
    start()
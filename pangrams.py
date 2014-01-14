# Created by JiaYi Lim on 13/1/2014

import sys

def pangrams(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = set()
    for c in string.lower():
        if c in alphabet:
            letters.add(c)
    missing = ''
    for i in alphabet:
        if i not in letters:
            missing += i
    return 'NULL' if not missing else missing

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            print pangrams(line)


if __name__ == '__main__':
    start()
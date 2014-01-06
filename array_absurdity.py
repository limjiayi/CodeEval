# Created by JiaYi Lim on 29/12/2013

import sys

def find_duplicate(nums):
    d = {}
    for n in nums:
        if d.get(n):
            return n
        else:
            d[n] = 1

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip().split(';')[1].split(',')
            line = [ int(c) for c in line ]
            print find_duplicate(line)

if __name__ == '__main__':
    start()
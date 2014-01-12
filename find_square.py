# Created by JiaYi Lim on 11/1/2014

import sys, math

def magnitude(c1, c2):
    return math.sqrt( abs(c1[0]-c2[0])**2 + abs(c1[1]-c2[1])**2 )

def is_square(coords):
    d = {}
    for i, c in enumerate(coords):
        remaining = coords[:i] + coords[i+1:]
        for r in remaining:
            mag = magnitude(c, r)
            d[mag] = d.get(mag, 1) + 1
    return len(d) == 2

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line != '':
                line = line.split(', ')
                line = [ eval(item.strip()) for item in line ]
                print 'true' if is_square(line) else 'false'


if __name__ == '__main__':
    start()
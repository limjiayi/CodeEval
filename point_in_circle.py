# Created by JiaYi Lim on 11/1/2014

import sys, math

def parse_coord(string):
    for i, c in enumerate(string):
        if c == '(':
            return eval(string[i:])

def parse_radius(string):
    for i, c in enumerate(string):
        if c == ':':
            return eval(string[i+2:])

def magnitude(c1, c2):
    return math.sqrt( abs(c1[0]-c2[0])**2 + abs(c1[1]-c2[1])**2 )

def point_in_circle(center, radius, point):
    if magnitude(center, point) > radius:
        return 'false'
    return 'true'

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.split(';')
            center = parse_coord(line[0])
            radius = parse_radius(line[1])
            point = parse_coord(line[2])
            print point_in_circle(center, radius, point)


if __name__ == '__main__':
    start()
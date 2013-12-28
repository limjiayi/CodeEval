# Created by JiaYi Lim on 27/12/2013

import sys, math

def magnitude(pt1, pt2):
    x1, y1 = pt1[0], pt1[1]
    x2, y2 = pt2[0], pt2[1]
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def closest_pair(points):
    shortest = float('inf')
    for i in range(len(points)-1):
        for j in range(i+1, len(points)):
            mag = magnitude(points[i], points[j])
            if mag < shortest:
                shortest = mag
    if shortest < 10**4:
        print '{0:.4f}'.format(shortest)
    else:
        print 'INFINITY'

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        points = []
        for line in f:
            line = line.strip().split()
            if len(line) != 1:
                line = [ int(c) for c in line ]
                points.append(line)
            elif len(points) != 0:
                closest_pair(points)
                points = []

if __name__ == '__main__':
    start()
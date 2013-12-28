# Created by JiaYi Lim on 25/12/2013

from collections import deque

def sum_digits(num):
    '''Sum the digits of a number'''
    total = 0
    while num > 0:
        total += num % 10
        num = num // 10
    return total

def accessible(point, maximum):
    '''A cell is accessible if the sum of the digits of its coords add up to <= max'''
    return  sum_digits(abs(point[0])) + sum_digits(abs(point[1])) <= maximum

def add_neighbours(pt, points, stack, maximum):
    r, c = pt[0], pt[1]
    for nbr in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
        if nbr not in points and accessible(nbr, maximum):
            points.add(nbr)
            stack.append(nbr)
    return points, stack

def monkey_grid(start, maximum):
    visited_points = set([start])
    stack = deque([start])
    i = 0
    while i < len(visited_points):
        current_pt = stack.popleft()
        visited_points, stack = add_neighbours(current_pt, visited_points, stack, maximum)
        i += 1
    print len(visited_points)

if __name__ == '__main__':
    monkey_grid(start=(0,0), maximum=19)
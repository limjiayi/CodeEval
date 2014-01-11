# Created by JiaYi Lim on 10/1/2014

import sys

def memo(func):
    cache = {}
    def wrapped(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapped

@memo
def rec_lcs(str1, str2):
    if not str1 or not str2:
        return ''
    if str1[-1] == str2[-1]:
        return rec_lcs(str1[:-1], str2[:-1]) + str1[-1]
    else:
        current1 = rec_lcs(str1[:-1], str2) # chop last char from str1
        current2 = rec_lcs(str1, str2[:-1]) # chop last char from str2
        return current1 if len(current1) > len(current2) else current2

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip().split(';')
            if line != ['']:
                print rec_lcs(line[0], line[1])


if __name__ == '__main__':
    start()
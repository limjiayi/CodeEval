# Created by JiaYi Lim on 26/12/2013

import sys

def replaceable(replaced, start, end):
    for tup in replaced:
        if start >= tup[0] and start <= tup[1]:
            return False
        elif end-1 >= tup[0] and end-1 <= tup[1]:
            return False
    return True

def subst_string(string, subst):
    replaced = []
    new_string = ''
    for i in range(0, len(subst), 2):
        start = 0
        while start < len(string):
            end = start + len(subst[i])
            check = string[start:end]
            if subst[i] == check and replaceable(replaced, start, end):
                if new_string == '':
                    new_string = string[:start] + subst[i+1] + string[end:]
                else:
                    new_string = new_string[:start] + subst[i+1] + new_string[end:]
                replaced.append((start, end-1))
                start = end
            else:
                start += 1
    return new_string

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip().split(';')
            string = line[0]
            subst = line[1].split(',')
            print subst_string(string, subst)

if __name__ == '__main__':
    start()
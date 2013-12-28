# Created by JiaYi Lim on 25/12/2013

import sys

def build_matrix(num_rows, num_cols, elements):
    matrix = []
    row = []
    for i in range(len(elements)):
        if (i+1) % num_cols != 0:
            row.append(elements[i])
        else:
            row.append(elements[i])
            matrix.append(row)
            row = []
    return matrix

def print_spiral(matrix):
    for i in range(len(matrix)/2 + 1):
        # print the top border
        for j in range(i, len(matrix[i])-i):
            print matrix[i][j],
        # print the right border
        for k in range(i+1, len(matrix)-1-i): 
            print matrix[k][-1-i],
        # print the bottom border
        # don't execute if we are at the middle row, to prevent duplicate printing
        if i != len(matrix) / 2:
            for m in reversed(range(i, len(matrix[i])-i)):
                print matrix[-1-i][m],
        # print the left border
        for n in reversed(range(i+1, len(matrix)-1-i)):
            print matrix[n][i],
    print

def start():
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line != '':
                line = line.split(';')
                num_rows = int(line[0])
                num_cols = int(line[1])
                elements = line[2].split()
                matrix = build_matrix(num_rows, num_cols, elements)
                print_spiral(matrix)


if __name__ == '__main__':
    start()
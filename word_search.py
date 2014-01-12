# Created by JiaYi Lim on 11/1/2014

import sys

def find_loc(board, letter):
    locations = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == letter:
                locations.append((i, j))
    return locations

def valid(board, r, c):
    return 0 <= r < len(board) and 0 <= c < len(board[0])

def search_adj(board, coord, letter):
    coords = []
    r, c = coord[0], coord[1]
    checks = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    for ch in checks:
        row, col = ch[0], ch[1]
        if valid(board, row, col) and board[row][col] == letter:
            coords.append((row, col))
    return coords

def word_search(board, word, results=[], history=[]):
    if len(word) == 1:
        return True
    if not results:
        results = find_loc(board, word[0])
    for res in results:
        letter = word[1]
        locs = search_adj(board, res, letter)
        locs = [ loc for loc in locs if loc not in history+[res] ]
        if not locs:
            continue
        return word_search(board, word[1:], locs, history+[res])
    return False

def start():
    board = [['A','B','C','D'],
             ['S','F','C','S'],
             ['A','D','E','E']]
    filepath = sys.argv[1]
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line != '':
                print word_search(board, line)


if __name__ == '__main__':
    start()
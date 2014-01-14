# Created by JiaYi Lim on 14/1/2014

import sys

def build_matrix(num_rows, num_cols, items):
	matrix = [ [ '.' for j in range(num_cols) ] for i in range(num_rows) ]
	for i, c in enumerate(items):
		if c == '*':
			row = i // num_cols
			col = i % num_cols
			matrix[row][col] = c
	return set_counts(matrix)

def num_mines(matrix, row_num, col_num):
	if 0 <= row_num < len(matrix):
		return sum([ 1 for idx, item in enumerate(matrix[row_num]) if abs(col_num-idx) <= 1 and item == '*' ])
	else:
		return 0

def set_counts(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j] == '.':
				adj_mines = num_mines(matrix, i-1, j) + num_mines(matrix, i, j) + num_mines(matrix, i+1, j)
				matrix[i][j] = adj_mines
	return matrix

def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			print matrix[i][j],
		print

def print_string(matrix):
	print ''.join([str(matrix[i][j]) for i in range(len(matrix)) for j in range(len(matrix[i]))])

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			line = line.strip()
			if line != '':
				line = line.split(';')
				rows, cols = line[0].split(',')
				items = line[1]
				matrix = build_matrix(int(rows), int(cols), items)
				print_string(matrix)


if __name__ == '__main__':
	start()
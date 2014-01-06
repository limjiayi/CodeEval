# Created by JiaYi Lim on 5/1/2013

import sys

def pascals_triangle(depth):
	# create a list of lists representation of Pascal's triangle to store the values
	cache = [ [0 for j in range(i)] for i in range(1, depth+1)]
	cache[0][0] = 1

	def retrieve(row, col):
		# if col is out of bounds, return 0
		if col < 0 or col > len(cache[row])-1:
			return 0
		return cache[row][col]

	for i in range(1, depth):
		for j in range(len(cache[i])):
			cache[i][j] = retrieve(i-1, j-1) + retrieve(i-1, j)

	for i in range(depth):
		for j in range(len(cache[i])):
			print cache[i][j],
	print

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			line = int(line.strip())
			pascals_triangle(line)


if __name__ == '__main__':
	start()
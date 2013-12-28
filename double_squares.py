# Created by JiaYi Lim on 26/12/2013

import sys

def sort_numbers(num1, num2):
	'''Sort so that the smaller number always comes first'''
	if num1 < num2:
		return (num1, num2)
	return (num2, num1)

def double_squares(num):
	'''Find the number of ways in which an integer can be written as the sum of 2 perfect squares'''
	# use a dictionary to cache (memoize) the perfect squares we will need to retrieve later
	cache = {}
	i = 0
	while i*i <= num:
		if not cache.get(i):
			cache[i*i] = i
		i += 1

	squares = set()
	for j in reversed(range(i)):
		remainder = num - j*j
		if cache.get(remainder):
			# solution has to be sorted before adding to the set to avoid duplicates
			solution = sort_numbers(j, cache[remainder])
			squares.add(solution)
	return len(squares)

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			num = int(line.strip())
			print double_squares(num)

if __name__ == '__main__':
	start()
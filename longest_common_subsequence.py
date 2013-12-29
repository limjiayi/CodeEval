# Created by JiaYi Lim on 28/12/2013

import sys

def find_char(string, char, pos):
	'''If the char is found in any position beyond the given pos, return its index, else return False'''
	for i in range(pos, len(string)):
		if char == string[i]:
			return True, i
	return False, None

def get_LCS(string1, string2):
	'''Return the longest common subsequence (need not be contiguous) between 2 strings'''
	LCS = ''
	max_len = 0
	# iterate through all possible starting positions of the LCS
	for i in range(len(string1)):
		current = ''
		pos = 0
		for j in range(i, len(string1)):
			char = string1[j]
			found, res = find_char(string2, char, pos)
			if found:
				pos = res
				current += char
		if len(current) > max_len:
			max_len = len(current)
			LCS = current
	return LCS.strip()

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			line = line.strip()
			if line != '':
				line = line.split(';')
				string1, string2 = line[0], line[1]
				print get_LCS(string1, string2)


if __name__ == '__main__':
	start()
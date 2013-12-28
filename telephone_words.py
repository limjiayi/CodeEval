# Created by JiaYi Lim on 26/12/2013

import sys

def telephone_words(string):
	d = {'0': '0', '1': '1', '2': 'abc', '3': 'def', 
	 '4': 'ghi', '5': 'jkl', '6': 'mno',
	 '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
	return permute(d, string)

def permute(d, string, current=''):
	if len(string) == 1:
		return d[string]
	else:
		perms = []
		for variant in d[string[0]]:
			remainders = permute(d, string[1:], current+variant)
			for r in remainders:
				perms.append(variant+r)
		return perms

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			line = line.strip()
			words = telephone_words(line)
			print ','.join(words)


if __name__ == '__main__':
	start()
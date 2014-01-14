# Created by JiaYi Lim on 14/1/2014

import sys

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			line = line.strip()
			if line != '':
				line = line.split()
				array = line[:-1]
				index = int(line[-1])
				if index <= len(array):
					print array[-index]

if __name__ == '__main__':
	start()
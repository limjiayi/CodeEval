# Created by JiaYi Lim on 8/1/2014

import sys

def predict_digit(pos):
	num_transitions = 0
	power = find_closest_power(pos)
	while pos > 0:
		pos -= 2**power
		num_transitions += 1
		power = find_closest_power(pos)
	if num_transitions == 0:
		return 0
	elif num_transitions % 3 == 0:
		return 0
	elif num_transitions % 3 == 1:
		return 1
	elif num_transitions % 3 == 2:
		return 2

def find_closest_power(num):
	i = 0
	while 2**i <= num:
		i += 1
	return i-1 if num >= 2 else 0

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			line = line.strip()
			if line != '':
				print predict_digit(int(line))


if __name__ == '__main__':
	start()
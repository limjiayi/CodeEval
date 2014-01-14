import sys

def sum_integers(lst):
	max_ending_here = max_so_far = lst[0]
	for item in lst[1:]:
		max_ending_here = max(item, max_ending_here+item)
		max_so_far = max(max_so_far, max_ending_here)
	return max_so_far

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			line = line.strip()
			if line != '':
				line = [ int(i.strip()) for i in line.split(',')]
				print sum_integers(line)


if __name__ == '__main__':
	start()
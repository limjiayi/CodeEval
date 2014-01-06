# Created by JiaYi Lim on 6/1/2014

import sys

def get_skyline(buildings):
	max_right = max([ b[2] for b in buildings ]) # get the length we need for our list of heights
	heights = [ 0 for i in range(max_right+1) ] # initialize all heights at 0

	for b in buildings:
		for j in range(b[0], b[2]):
			if b[1] > heights[j]:
				heights[j] = b[1] # overwrite previous height if the new height is taller

	skyline = []
	p = 1 # toggled to 0 when we encounter the left edge of the first building
	prev_h = None
	for idx, h in enumerate(heights):
		if p and h == 0: continue # skip if we haven encountered the first building
		elif h != prev_h:
			skyline.extend([idx, h])
			prev_h = h
			p = 0

	return skyline

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			if line != ' ':
				line = line.strip().split(';')
				if line != ['']:
					line = [ eval(tup) for tup in line ]
					skyline = get_skyline(line)
					for num in skyline:
						print num,
					print


if __name__ == '__main__':
	start()
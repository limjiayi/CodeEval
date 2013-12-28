import sys

class Person(object):
	def __init__(self, data):
		self.data = data
		self.alive = True
		self.next = None

class LinkedList(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def add_node(self, node):
		if self.head:
			current = self.head
			self.tail.next = node
			self.tail = node
		else:
			self.head = node
			self.tail = node

def create_linked_list(n):
	circle = LinkedList()
	for i in range(n):
		new_node = Person(i)
		circle.add_node(new_node)
	# make the linked list circular by connecting the tail to the head
	circle.tail.next = circle.head
	return circle

def print_order(circle, n, m):
	# kill every mth person
	count = 0
	num_printed = 0
	current = circle.head
	while num_printed < n:
		if current.alive:
			count += 1
			if count == m:
				print current.data,
				num_printed += 1
				current.alive = False
				count = 0
		current = current.next
	print

def start():
	filepath = sys.argv[1]
	with open(filepath) as f:
		for line in f:
			line = line.strip().split(',')
			n = int(line[0])
			m = int(line[1])
			circle = create_linked_list(n)
			print_order(circle, n, m)


if __name__ == '__main__':
	start()
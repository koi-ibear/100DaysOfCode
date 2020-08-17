"""
2.4 Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""

class Node:
	'''
	create a node
	'''
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	'''
	linked list operations
	'''
	def __init__(self):
		'''
		initiiate with empty head
		'''
		self.head = None
	def push(self, new_data):
		'''
		insert new_data at the beginning of a linked list
		'''
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
	def dataList(self):
		res = []
		cur_node = self.head
		while cur_node is not None:
			res.append(cur_node.data)
			cur_node = cur_node.next
		return res
	def partition(self, x):
		orig_head = head = Node(0)
		orig_tail = tail = Node(0)
		node = self.head
		while node:
			if node.data < x:
				head.next = node
				head = head.next
			else:
				tail.next = node
				tail = tail.next
			node = node.next
		tail.next = None
		head.next = orig_tail.next
		return orig_head.next


## test - 2.2
ll = LinkedList()
ll.push(4)
ll.push(5)
ll.push(1)
ll.push(4)
ll.push(8)
ll.push(1)
node = ll.partition(2)
res = []
while node:
	res.append(node.data)
	node.next
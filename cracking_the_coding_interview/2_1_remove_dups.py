"""
2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?
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
	def insertAfter(self, prev_node, new_data):
		'''
		insert new_data after prev_node in a linked list
		'''
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node
	def append(self, new_data):
		'''
		append new_data at the end of a linked list
		'''
		new_node = Node(new_data)
		if self.head is None:
			self.head = new_node
		tail = self.head
		while tail.next:
			tail = tail.next
		tail.next = new_node
	def removeNode(self, node):
		if self.head.data == node.data:
			self.head = self.head.next
		else:
			cur_node = self.head
			while cur_node is not None:
				if cur_node.next.data == node.data:
					cur_node.next = cur_node.next.next
					break
				else:
					cur_node = cur_node.next
	def dataList(self):
		res = []
		cur_node = self.head
		while cur_node is not None:
			res.append(cur_node.data)
			cur_node = cur_node.next
		return res
	def removeDup(self):
		found = set()
		cur_node = self.head
		found.add(cur_node.data)
		while cur_node is not None:
			if cur_node.next.data in found:
				cur_node.next = cur_node.next.next
			else:
				found.add(cur_node.next.data)
			cur_node = cur_node.next
	def kToLast(self, k):
		## two-pointers
		n0 = n1 = self.head
		step = 0
		while step < k:
			n1 = n1.next
			step += 1
		while n1 is not None:
			n0 = n0.next
			n1 = n1.next
		return n0

## test - 2.1
ll = LinkedList()
ll.push(4)
ll.push(5)
ll.push(1)
ll.push(4)
ll.push(8)
ll.push(1)
ll.dataList()
ll.removeDup()
ll.dataList()


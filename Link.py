#!/usr/bin/python

class Node(object):
	"""Single node for use in a linked list"""
	value = None #value of the node
	after = None #next node
	
	def __init__(self,value):
		"""initialize a node with value"""
		self.value = value
		
class Link(object):
	"""Class to manage linked list attributes and methods"""
	head = None
	tail = None	
	
	def __init__(self):
		"""initialize an empty linked list"""
		pass
		
		
	def addFirst(self, node):
		"""adds node to the begining of the list"""
		if(node is not None and type(node) is Node):
			if(self.head is None):
				self.head = node
				self.tail = node
			else:
				node.after = self.head
				self.head = node
	

	def addLast(self, node):
		"""adds the node to the end of the list"""
		if(node is not None and type(node) is Node):
			if(self.tail is None):
				self.tail = node
				self.head = node
			else:
				self.tail.after = node
				self.tail = node 
			
	def removeFirst(self):
		"""removes the first node in the list"""
		self.head = self.head.after

	def removeLast(self):
		"""removes the last node in the list"""
		node = self.head
		while(node.after is not self.tail):
			node = node.after
		node.after = None

	def removeNode(self, trash):
		"""removes a given node from the list"""
		if(trash is not None and type(trash) is Node):
			node = self.head
			while(node is not None and node.after is not trash):
				node = node.after
			if(node.after is trash):
				nextnode = trash.after
				node.after = nextnode

	def printList(self):
		"""prints the linked list starting with the head"""
		node = self.head
		while(node is not None):
			print node.value
			node = node.after
	
	def convertToList(self):
		"""
		converts self to a pythonic list

		return:
		list with nodes as elements
		"""
		node = self.head
		result = []
		while(node is not None):
			result.append(node.value)
			node = node.after
		return result

if(__name__=="__main__"):
	myLink = Link()
	first = Node(3)
	middle = Node(5)
	last = Node(7)
	berry = Node(10)
	cherry = Node(2)
	merry = Node(1)
	
	myLink.addFirst(first)
	myLink.addLast(middle)
	myLink.addLast(last)
	myLink.addFirst(berry)
	myLink.addLast(cherry)
	myLink.addLast(merry)
	print "Initial list:"
	myLink.printList()

	myLink.removeFirst()
	myLink.removeLast()
	myLink.removeNode(middle)
	print "Removed first, last and middle"
	myLink.printList()

	result = myLink.convertToList()
	print "As a python list:"
	print result

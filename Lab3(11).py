class Node():
	def __init__(self, data = None):
		self.data = data
		self.next = None
		self.pred = None
	def __str__(self):
		return f"{self.pred}"
class DoublyLinkedList:
	def __init__(self):
		self.head = None
		self.last = None
	def __str__(self):
		if self.head is None:
			return"List has no element"
		else:
			a = self.head
			s = ""
			while a is not None:
				s+= str(a.data)
				if a.next is not None:
					s+="->"
				a = a.next
			return s
	def delstart(self): # удаление первого элемента
		if self.head is None:
			return None
		if self.head.next is None:
			self.head = None
			return
		self.head = self.head.next
		self.last = None
	def delend(self): # удаление последнего элемента
		if self.head is None:
			return None
		if self.head.next is None:
			self.head = None
			return
		a = self.head
		while a.next is not None:
			a = a.next
		a.pred.next = None
	def delk(self, k): # удаление элемента = к
		if self.head is None:
			return None
		if self.head.next is None:
			if self.head.data == k:
				self.head = None
			else:
				return None
		if self.head.data == k:
			self.head = self.head.next
			self.head.pred = None
			return
		a = self.head
		while a.next is not None:
			if a.data == k:
				break;
			a = a.next
		if a.next is not None:
			a.pred.next = a.next
			a.next.pred = a.pred
		else:
			if a.data == k:
				a.pred.next = None
			else:
				return None
	def addend(self, data): # Добавление в конец
		if self.head is None:
			a = Node(data)
			self.head = a
			return
		n = self.head
		while n.next is not None:
			n = n.next
		a = Node(data)
		n.next = a
		a.pred = n
	def addstart(self, data): # Добавление в начало
		if self.head is None:
			a = Node(data)
			self.head = a
			return None
		a = Node(data)
		a.next = self.head
		self.head.pred = a
		self.head = a


if __name__ == '__main__':
	linlist = DoublyLinkedList()
	node1 = Node(1)
	linlist.head = node1
	node2 = Node(2)
	node3 = Node(3)
	node4 = Node(4)
	node5 = Node(4)
	linlist.last = node5
	node1.next = node2
	node2.next = node3
	node3.next = node4
	node4.next = node5
	node2.pred = node1
	node3.pred = node2
	node4.pred = node3
	node5.pred = node4
	print(linlist)
	linlist.delstart()
	print(linlist)
	linlist.delend()
	print(linlist)
	linlist.delk(3)
	print(linlist)
	linlist.addend(6)
	print(linlist)
	linlist.addstart(6)
	print(linlist)
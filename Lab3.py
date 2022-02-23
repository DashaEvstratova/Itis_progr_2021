class Node():
  def __init__(self, data = None):
    self.data = data
    self.next = None
  def __str__(self):
    return f"[{self.data}]->{self.next}"


class LinkedList():
	def __init__(self, a):
		self.head = None
		with open(a) as f:
			n = int(f.readline())
			a = int(f.readline())
			a = Node(a)
			self.head = a
			for i in range(0, n-1):
				b = int(f.readline())
				b = Node(b)
				a.next = b
				a = b
	def __str__(self):
		return str(self.head)
	def delAllk(self): # Удаление элементов сумма цифр в котором > 10
		a = self.head
		b = a
		k = 0
		c = a.data
		while c!=0:
			k +=c%10
			c = c//10
		if k > 10:
			self.head = self.head.next
		while a:
			c = a.data
			k = 0
			while c!=0:
				k += c%10
				c = c//10
			if k > 10:
				b.next = a.next
			b = a
			a = a.next
		if a == None:
			return
		b.next = a.next
		a = None
	def delAll2(self): # Удаление каждого второг и к каждому первому прибавка второго
		a = self.head
		b = a
		c = 0
		self.head.data += self.head.next.data
		while a.next:
			c+=1
			if c%2==1 and c >2:
				a.data += a.next.data
			else:
				b.next = a.next
			b = a
			a = a.next
		if a == None:
			return
		b.next = a.next
		a = None
	def Serch(self): # Поменять минимальный и максимальный элемент
		maxs = 0
		a = self.head
		while a:
			if a.data > maxs:
				maxs = a.data
			a = a.next
		mins = 1000000
		a = self.head
		while a:
			if a.data < mins:
				mins = a.data
			a = a.next
		a = self.head
		while a:
			if a.data == maxs:
				a.data = mins
			elif a.data == mins:
				a.data = maxs
			a = a.next
	def revers(self):
		a = None
		b = self.head
		c = self.head.next
		while c:
			b.next = a
			a = c
			c = c.next
		b.next = a
		b = None
if __name__ == '__main__':
	linlst = LinkedList(input())
	print(linlst)
	linlst.delAllk()
	print(linlst)
	linlst.delAll2()
	print(linlst)
	linlst.Serch()
	print(linlst)
	linlst.revers()
	print(linlst)
	print(0)

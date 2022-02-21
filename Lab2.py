class Node():
  def __init__(self, data = None):
    self.data = data
    self.next = None
  def __str__(self):
    return f"[{self.data}]->{self.next}"
  


class LinkedList:
  def __init__(self):
    self.head = None
  def __str__(self):
    return str(self.head)
  def leng(self): #Длина списка
    count = 0
    a =  self.head
    while a:
      count +=1
      a = a.next
    return count
  def maks(self): # Максимальный элемент
    maxs = 0
    a = self.head
    while a:
      if a.data > maxs:
        maxs = a.data
      a = a.next
    return maxs
  def minus(self): # Наличие отрицательных числе
    a = self.head
    while a:
      if a.data <0:
        return "Yes"
      a = a.next
    return "No"
  def delK(self, k): # Удаление k элемента
    a = self.head
    if a:
      if a.data == k:
        self.head = a.next
        a = None
        return
    while a:
    	if a.data == k:
    		break
    	b = a
    	a = a.next
    if a == None:
    	return
    b.next = a.next
    a = None
  def delAllk(self, k): # Удаление всех элементов = k
    a = self.head
    while a:
    	b = a
    	if a.data == k:
        	b.next = a.next
      	b = a
      	a = a.next
    if a == None:
    	return
    b.next = a.next
    a = None
  def addend(self, new):
    pass
  def Del(self): # Удаление первого элемента
    self.head = self.head.next
  def Delend(self): # Удаление последнего элемента
    a = self.head
    if not a:
      return 
    while a.next:
      b = a
      a = a.next
    if a == None:
      return
    b.next = a.next
    a = None
  def Delprend(self): # Удаление предпоследнего элемента
    a = self.head
    if not a:
      return 
    while a.next:
      b = a
      a = a.next
    b.data = a.data
    b.next = a.next
    if a == None:
      return
  def Search(self, k):
    a = self.head
    c = 1
    while a:
      if c == k:
        return a.data
      a = a.next
      c+=1
    return None
  def isEmpty(self):
    if self.head == None:
      return "True"
    else:
      return "False"
  def InsertAtEnd(self, new): # Вставка в конец
    new = Node(new)
    a = self.head
    while a.next:
      b = a
      a = a.next
    a.next = new
  def InsertAtHead(self, new): # вставка в начало
    new = Node(new)
    a = self.head
    self.head = new
    while a:
      b = new.next
      new.next = a
      a= b
      new = new.next
  def InsertAtpr(self, new): # Вставка после первого элемента
    new = Node(new)
    a = self.head.next
    while a.next:
      b = a.data
      a.data = new.data
      new.data = b
      a = a.next
    b = a.data
    a.data = new.data
    a.next = Node(b)
if __name__ == '__main__':
  linlst = LinkedList()
  node1 = Node(1)
  linlst.head = node1
  node2 = Node(2)
  node3 = Node(3)
  node4 = Node(4)
  node5 = Node(5)
  node6 = Node(6)
  node7 = Node(4)
  node1.next = node2
  node2.next = node3
  node3.next = node4
  node4.next = node5
  node5.next = node6
  node6.next = node7
  print(linlst)
  print(linlst.leng())
  print(linlst.maks())
  print(linlst.minus())
  linlst.Del()
  print(linlst)
  linlst.delK(3)
  print(linlst)
  linlst.Delend()
  print(linlst)
  linlst.delAllk(4)
  print(linlst)
  linlst.Delprend()
  print(linlst)
  print(linlst.Search(2))
  print(linlst.isEmpty())
  linlst.InsertAtEnd(8)
  print(linlst)
  linlst.InsertAtHead(8)
  print(linlst)
  linlst.InsertAtpr(7)
  print(linlst)
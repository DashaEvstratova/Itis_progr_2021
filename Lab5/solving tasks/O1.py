a = input()
x1 = a.find('f')
x2 = a.rfind('f')
if x1 == x2 and x1 != -1:
	print(x1) 
elif x1 != x2:
	print(x1, x2)
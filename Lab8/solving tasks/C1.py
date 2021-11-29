def prc(n):
	q=[]
	i = int(n**(1./3.))
	while n != 0:
		if n >= i**3:
			n -= i**3
			q.append(i**3)
		else:
			i -= 1
	if len(q)<=7:
		print(*q)
	else:
		print(0)
prc(5)
prc(22)
prc(2)
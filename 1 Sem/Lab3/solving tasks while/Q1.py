a = int(input())
i = 1
n = 0
n1 = 0
n2 = 1
if a == 0:
	print('1')
elif a == 1:
	print('2')
else:
	while n2 < a:
		n1 = n2
		n2 = n + n2
		n = n1
		i = i + 1
if n2 == a:
	print(i)
else:
	print(-1)
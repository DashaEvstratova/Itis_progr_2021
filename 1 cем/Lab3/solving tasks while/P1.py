a = int(input())
i = 1
n = 0
n1 = 0
n2 = 1
if a == 1:
	print('0')
elif a == 2:
	print('1')
else:
	while i != a:
		n1 = n2
		n2 = n + n2
		n = n1
		i = i + 1
print(n2)
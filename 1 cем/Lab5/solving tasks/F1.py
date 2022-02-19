n = int(input())
x = float(input())
n1 = 0
for i in range(n):
	n2 = float(input())
	n1 = (n1 + n2) * x
n2 = float(input())
n1 = n1 + n2
print(n1)
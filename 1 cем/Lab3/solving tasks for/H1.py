a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
k = 0
for i in range(0, 1001):
	if (a*(i**3) + b*(i**2) + c*i +d == 0) and (i != e):
		k += 1
print(k)
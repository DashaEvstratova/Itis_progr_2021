n = int(input())
s = 0
for i in range(1, n + 1):
	s = s + i
for i in range(n-1):
	a = int(input())
	s = s - a
print(s)
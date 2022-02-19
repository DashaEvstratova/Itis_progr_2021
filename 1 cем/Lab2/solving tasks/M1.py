a = int(input())
b = int(input())
c = int(input())
if a <= c <= b:
	(a, b, c) = (a, c, b)
elif c <= b <= a:
	(a, b, c) = (c, b, a)
elif c <= a <= b:
	(a, b, c) = (c, a, b)
elif b <= a <= c:
	(a, b, c) = (b, a, c)
elif b <= c <= a:
	(a, b, c) = (b, c, a)
print(a, b, c)
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
if (d >= c and e >= a) or (d >= a and e >= c):
	print('YES')
elif (d >= c and e >= b) or (d >= b and e >= c):
	print('YES')
elif (d >= b and e >= a) or (d >= a and e >= b):
	print('YES')
else:
	print('NO')
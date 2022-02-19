a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and c + b > a:
	if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
		print('rectangular')
	elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or c**2 + b**2 < a**2:
		print('obtuse')	
	elif a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or c**2 + b**2 > a**2:
		print('acute')
else:
	print('impossible')
n = int(input())
if n % 10 == 1:
	print(n, 'korova')
elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
	print(n, 'korovy')
else:
	print(n, 'korov')
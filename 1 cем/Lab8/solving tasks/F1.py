def god(a, b):
	if a * b == 0:
		print(a + b)
	else:
		if a < b:
			god(a, b % a)
		else:
			god(a % b, b)

god(1, 1)
god(2, 1)
god(2, 2)
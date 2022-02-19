for i in range(10, 100):
	a = i // 10
	b = i % 10
	if a * b * 2 == i:
		print(i)
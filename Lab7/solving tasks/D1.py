N = int(input())
a = list(map(int, input(). split(' ')))
m = int(input())
b = list(map(int, input().split(' ')))
c = 1000
for i in a:
	for j in range(0, m):
		e = abs(b[j] - i) # расстояние между i пункт и j убежища
		if e < c: # нахождени минимального расстояния между i пунктом и убежищами
			c = e
			h = j + 1
	print(h, end=' ') # вывод ближайшего убежища
	c = 1000
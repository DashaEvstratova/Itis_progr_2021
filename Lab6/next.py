from decimal import Decimal
with open('primer.txt') as f:
	l = open('result.txt', 'w') # файл с результатом
	S = int(f.readline())
	U = int(f.readline())
	N = int(f.readline())
	for i in range(0, N):
		# создается массив
		q = []
		for i in range(S):
			w = [0] * S
			q.append(w)
		# заполнение i  массива 
		a = list(map(int, f.readline().strip()))
		for j in range(1, len(a)):
			q[a[j - 1]][a[j]] += 1
		# деление каждого элемента матрицы для постойки биграмм
		for j in range(0, S):
			for h in range(0, S):
				q[j][h] = (Decimal(q[j][h]) / Decimal(N-1)).quantize(Decimal('1.00'))
				#запись в файл каждый элемент i матрицы
				l.write(str(q[j][h]) + ' ')
			#переход на следующую строку
			l.write('\n')
		#переход на следующую матрицу
		l.write('\n')
l.close()
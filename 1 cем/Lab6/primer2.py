import random
from decimal import Decimal

f = open('primer2.txt', 'w')
S = int(input())#способность
U = int(input())#размер последовательности
N = int(input())#количество последовательности
f.write(str(S) + '\n')
f.write(str(U) + '\n')
f.write(str(N) + '\n')
for i in range(N):
	for j in range(U):
		q = str(random.randrange(0, S, 1))
		f.write(q) #добавление j элемента в файл i последовательности
	f.write('\n')
f.close()

with open('primer2.txt') as f:
	l = open('result2.txt', 'w') # файл с результатом
	S = int(f.readline())#способность
	U = int(f.readline())#размер последовательности
	N = int(f.readline())#количество последовательности
	for i in range(0, N):
		a = list(map(int, f.readline().strip())) #чтение и перевод строки последовательности
		dct = dict() # создание словаря
		for i in range(1, len(a)):
			h = str(a[i-1]) + str(a[i]) # создание ключа-биграммы по последовательности
			dct[h]= dct.get(h,0)+1 # счетчик в словаре по ключу-биграммы
		for i in range(0, S):
			for j in range(0, S):
				h = str(i)+str(j) # все возможные биграммы
				if h in dct:
					l.write(str((Decimal(dct[h]) / (N-1)).quantize(Decimal('1.00'))) + ' ') # если такая биграмма есть, то заменяем ее на ее частоту
				else:
					l.write('0,00' + ' ') # в противном случае записываем 0.00
			l.write('\n') #переход на новою строку
		l.write('\n') #переход на новую матрицу
l.close()
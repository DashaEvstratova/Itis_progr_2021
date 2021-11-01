import random
f = open('primer.txt', 'w')
#способность
S = int(input())
#размер последовательности
U = int(input())
#количество последовательности
N = int(input())
f.write(str(S) + '\n')
f.write(str(U) + '\n')
f.write(str(N) + '\n')
for i in range(N):
	for j in range(U):
		q = str(random.randrange(0, S, 1))
		f.write(q) #добавление j элемента в файл i последовательности
	f.write('\n')
f.close()
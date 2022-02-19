N = int(input())
dct = dict()
for i in range(N): # цикл для ввода всех строк
	q = list(input().split(' ')) # чтение строки
	dct[q[0]] = q[1] # добавление в словарь 
a = input()
if a in dct: # проверка чем является слово, ключ или значение
	print(dct[a])
else: # если ключ
	for k, v in dct.items(): # проходимся по словарю и ищем наше значение, после чего выводим значение ключа
		if v == a:
			print(k)
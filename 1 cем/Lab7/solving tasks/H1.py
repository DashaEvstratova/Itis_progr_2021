from collections import defaultdict

clients = defaultdict(lambda: defaultdict(int))
n = 0
q = []
while n != '':
	n = input()
	q.append(n) # создание массива со всеми строками
q.pop(-1)
for i in q:
	client, thing, value = i.split(' ') # распаковка элементов массива
	clients[client][thing] += int(value) # добавление в словарь
for client in sorted(clients): # вывод клиентов по алфавиту
	print(client + ':')
	for thing in sorted(clients[client]): # вывод покупок по алфавиту
		print(thing, clients[client][thing])
n = 0
q = ''
while n != '': # ввод сторк пока не введется пустая
	n = input()
	if n is not '':
		q += ' '
		q += n
dct = dict()
q = q.split(' ') # набор всех слов
for i in q:
	if i is not "":
		dct[i]= dct.get(i,0) + 1 # счет всех слов в словаре
dictionary = []
for k, v in dct.items(): # создаем список на основе словаря для сортироки
		dictionary.append((k, v))
dictionary = sorted(dictionary)[::-1] # обратная сортировка словаря по первым буквам слов
dictionary.sort(key = lambda x: x[1]) # сортировка по количесту слов
dictionary = dictionary[::-1] # переворачиваем список
for i in dictionary:
	print(i[0])
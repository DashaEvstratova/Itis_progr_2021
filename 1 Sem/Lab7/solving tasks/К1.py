N = int(input())
dct = dict() # Словарь ключ-ребенок, значение-родитель
dct1 = dict() # Словарь со всеми людьми, у которых все значения по умолчанию 0
for i in range(N-1):
	a = input().split()
	dct[a[0]] = a[1] # Добавление пар детей и родителей
	dct1[a[0]] = 0 # Добавление всех людей со значением 0
	dct1[a[1]] = 0 # Добавление всех людей со значением 0
for i in dct:
	r = i
	while r in dct: # проход пословарю пока человек является родителем
		r = dct[r] # переход на родителя этого родителя
		dct1[i] += 1 # пока заходим в цикл увеличиваем покаления
for i in sorted(dct1): # вывод отсортированного словаря
	print(i, dct1[i])
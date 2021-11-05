s = list()
g = True
for i in range(8):
	s.append(input()) # ввод координат, где стоят ферзи
for i in range(0, len(s)):
	s[i] = int(s[i][0]) + int(s[i][-1]) # Замена координат на их сумму
for i in s: # Проход по всему списку
	if s.count(i) > 1: #Если сумма повторяется, это значит, что они стоят на одной диагонали 
		g = False
		break
if not g: #Если все суммы не по одному разу встречаются, то вывести да
	print('YES')
else: # В противном случае нет
	print('NO')
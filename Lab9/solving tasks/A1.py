from copy import deepcopy
from sys import stdin
class Matrix:
	def __init__(self, matrix):
		self.matrica = deepcopy(matrix) # Создается копия массива
	def __str__(self):
		string = ''
		for i in self.matrica:
			for j in i:
				string += '%s\t' % j # Вывод матрицы через табуляцию
			string = string[:-1]
			string += '\n'
		string = string[:-1]
		return string
	def size(self):
		return (len(self.matrica), len(self.matrica[0])) # Возвращает размеры матрицы
a = Matrix([[3, 5, 7], [5, 6, 8]])

exec(stdin.read())
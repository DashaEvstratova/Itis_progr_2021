from copy import deepcopy

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
	def __add__(self, other):
		result = []
		s = []
		for i in range(0, len(self.matrica)):
			for j in range(0, len(self.matrica[0])):
				res = self.matrica[i][j] + other.matrica[i][j] # Сложение каждого элемента двух матриц
				s.append(res)
			result.append(s)
			s = []
		return Matrix(result)
	def __mul__(self, other):
		if isinstance(other, int) or isinstance(other, float): # Проверка, что первая матрица,а второе число
			result = []
			s = []
			for i in range(0, len(self.matrica)):
				for j in range(0, len(self.matrica[0])):
					res = self.matrica[i][j] * other # Умножение каждого элемента матрицы на заданное число
					s.append(res)
				result.append(s)
				s = []
		return Matrix(result)
	__rmul__ = __mul__ 


m = Matrix([[1, 1, 0], [0, 2, 10], [10, 15, 30]])
alpha = 15
print(m * alpha)
print(alpha * m)

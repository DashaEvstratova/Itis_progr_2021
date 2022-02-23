from copy import deepcopy

class MatrixError(BaseException):
	def __init__(self, matrix1, other):
		self.matrix1 = matrix1
		self.matrix2 = other
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
	@staticmethod
	def size(self):
		return (len(self.matrica), len(self.matrica[0])) # Возвращает размеры матрицы
	def __add__(self, other):
		if self.size(self) == self.size(other):
			result = []
			s = []
			for i in range(0, len(self.matrica)):
				for j in range(0, len(self.matrica[0])):
					res = self.matrica[i][j] + other.matrica[i][j] # Сложение каждого элемента двух матриц
					s.append(res)
				result.append(s)
				s = []
			return Matrix(result)
		else:
			error = MatrixError(self, other)
			raise error
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
	def transpose(self): # Транспонирование матрицы
		b =[]
		s = [0]*len(self.matrica)
		for i in range(0, len(self.matrica[0])):
			b.append(s) # Создание матрицы b такого же размера как и изначальная
		for i in range(0, len(self.matrica[0])):
			for j in range(0, len(self.matrica)):
				b[i][j] = self.matrica[j][i] # Заполнение массива b заркально отображенной относительно главной диагонали изначальной матрицы
		self.matrica = b
		return Matrix(self.matrica)
	@staticmethod
	def transposed(self): # Транспонирование матрицы
		b =[]
		s = [0]*len(self.matrica)
		for i in range(0, len(self.matrica[0])):
			b.append(s) # Создание матрицы b такого же размера как и изначальная
		for i in range(0, len(self.matrica[0])):
			for j in range(0, len(self.matrica)):
				b[i][j] = self.matrica[j][i] # Заполнение массива b заркально отображенной относительно главной диагонали изначальной матрицы
		return Matrix(b)


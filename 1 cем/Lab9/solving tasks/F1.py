from copy import deepcopy
import numpy as np
class MatrixError(BaseException):
	def __init__(self, matrix1, other):
		self.matrix1 = matrix1
		self.matrix2 = other
class Matrix:
	def __init__(self, matrix):
		self.matrica = deepcopy(matrix)  # Создается копия массива
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
		return len(self.matrica), len(self.matrica[0]) # Возвращает размеры матрицы
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
		elif isinstance(other, Matrix):  # Проверка, что первая матрица,а второе матрица
			if self.size(self)[1] == self.size(other)[0]: # Проверка на совпадение размеров
				s = []
				res = []
				c = 0
				for i in range(0, self.size(self)[0]):
					for t in range(0, self.size(other)[1]):
						for j in range(0, self.size(self)[1]):
							c = self.matrica[i][j] * other.matrica[j][t] + c # Перемножение матриц
						s.append(c)
						c = 0
					res.append(s)
					s = []
				return Matrix(res)
			else: # В противном случае вызвать ошибку
				error = MatrixError(self, other)
				raise error
		return Matrix(result)
	__rmul__ = __mul__
	def transposed(self): # Транспонирование матрицы
		b =[]
		s = [0]*len(self.matrica)
		for i in range(0, len(self.matrica[0])):
			b.append(s) # Создание матрицы b такого же размера как и изначальная
		for i in range(0, len(self.matrica[0])):
			for j in range(0, len(self.matrica)):
				b[i][j] = self.matrica[j][i] # Заполнение массива b заркально отображенной относительно главной диагонали изначальной матрицы
		return Matrix(b)
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
	def solve(self, massiv): # Решение системы матрицы
		res = []
		det = np.linalg.det(self.matrica) # Определитель основоной матрицы
		if det !=0 : # Проверка чтб определитель не 0
			for i in range(0, len(self.matrica[0])):
				b = deepcopy(self.matrica) # Копирование матрицы
				for j in range(0, len(self.matrica)):
					b[j][i] =  massiv[j] # Замена J столбца на массив  
				n = np.linalg.det(b) # Нахождение определителя
				res.append(round(n/det, 2)) # Ответ на каждую перерменной
			return str(res)[1:-1].replace(',', ' ')
		else: # В противном случае выдать ошибку
			error = MatrixError(self, other)
			raise error

class SquareMatrix(Matrix):
	def __pow__(self, deg):
		b = Matrix(self.matrica) # Копирование матрицы
		d = Matrix(self.matrica) # Копирование матрицы
		if deg > 1: # Если степень больше первой, то перемножаем матрицы
			for i in range(deg-1):
				a =  d*b
				b = a
			return b
		elif deg == 1: # Если степень равна 1, то просто выводим матрицу
			return Matrix(self.matrica)
		elif deg == 0: # Если степень равна нулю, то все отличные от нуля числа заменяем на 1
			for i in range(2, 10):
				str(self.matrica).replace(str(i), '1')
			return Matrix(self.matrica)


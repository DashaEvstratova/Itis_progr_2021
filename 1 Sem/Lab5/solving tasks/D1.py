from decimal import Decimal
n = Decimal(input())
n = int(n * 100)
x = n // 100
y = n % 100
print(x, y)
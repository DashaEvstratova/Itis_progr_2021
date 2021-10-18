p = int(input())
x = int(input())
y = int(input())
x = 100 * x + y
x = int(x * (100 + p) / 100)
print(x // 100, x % 100)
import math
n = int(input())
x = float(input())
for i in range(n-1):
      x = x + math.cos(x)
print(math.cos(x))
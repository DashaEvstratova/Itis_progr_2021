n = int(input())
x = float(input())
res = 0
for i in range(n+1):
      a = int(input())
      res = res + a*(x**i)
print(res)
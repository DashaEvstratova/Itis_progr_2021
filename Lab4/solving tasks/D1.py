n = int(input())
x = float(input())
s = 0
c = 1
for i in range(1, n+1):
      c = c * (x + i)
      s = s + c
print(s)
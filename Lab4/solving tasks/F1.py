n = int(input())
n1 = n
for i in range(n):
      print('*'*n1, '0'*(i*2 + 1), '*'*n1,sep='', end='')
      print()
      n1 -= 1
n1 = 2*n - 1
print('0'*(2*n + 1))
for i in range(1, n+1):
      print('*'*i, '0'*n1, '*'*i,sep='', end='')
      print()
      n1 -= 2
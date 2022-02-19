n = int(input())
n1 = n
step = 0
q = []
q.append(n)
for i in range(0, n+1):
      print('*'*n, '0'*(2*n1+1-2*n), '*'*n, sep='', end='')
      print()
      step += 1
      if n % 2 == 0:
            if step == 1:
                  c = n // 2 -1
            n = n - (n // 2 - 1)
      elif n % 2 != 0 and n != 1:
            if step == 1:
                  c = (n -1) // 2
            n = n - ((n - 1) // 2)
      if n1 - step == c:
            n = 1
      if step == n1:
            n = 0
      q.append(n)
q = q[:n1]
q = q[::-1]
for i in range(0, n1):
      print('*'*q[i], '0'*(2*n1 + 1 - q[i]*2), '*'*q[i], sep='', end='')
      print()
n = int(input())
width = 1
width1 = 1
i = 1
while i != n:
      width1 += 2
      i +=1
width = width1
for i in range(1, n+1):
      print(' '*width1, '*'*((i*2)-1), ' '*width1, sep='', end='')
      width1 = width1 - 1
      print()
for i in range(1, n + 1):
      print(' '*width1, '*'*((i*2)-1), ' '*width, '*'*((i*2)-1), sep='', end='')
      width -= 2
      width1 -=1
      print()
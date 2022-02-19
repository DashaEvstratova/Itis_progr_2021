n = int(input())
radius = (((n // 2)**2) // 2)**0.5
for i in range(n, -n-1, -1):
      for j in range(-n, n+1):
            if i**2 + j**2 <= n**2:
                  if (j + radius)**2 + (i - radius)**2 <= (n // 2)**2:
                        print('0', end='')
                  elif j <= 0 and i >= 2*radius:
                        print('0', end='')
                  elif (j - radius)**2 + (radius + i)**2 > (n // 2)**2 and j >= 0 and i >= 0:
                        print('0', end='')
                  elif (j - radius)**2 + (radius + i)**2 > (n // 2)**2 and j >= 2 * radius and i <= 0:
                        print('0', end='')
                  else:
                        print('1', end='')
            else:
                  print(' ', end='')
      print(' ')
for n in range(1, 5001):
      n1 = n
      s = 0
      if n > 2:
            for i in range(1, n):
                  if n % i == 0:
                        s += i
                        n = n // i
      if n1 == 1 or n1 == s:
            print(n1)
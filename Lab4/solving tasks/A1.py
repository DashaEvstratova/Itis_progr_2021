n = int(input())
sum_nch = 0
prois_ch = 1
sum_minus = 0
prois_plus = 1
for i in range(n):
      a = int(input())
      if a > 0:
            prois_plus *= a
      if a < 0:
            sum_minus += a
      if a % 2 == 0:
            prois_ch *= a
      if a % 2 != 0:
            sum_nch += a
print(sum_nch)
print(prois_ch)
print(sum_minus)
print(prois_plus)
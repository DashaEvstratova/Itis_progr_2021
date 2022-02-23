n = int(input())
i = 0
while n > 0:
    c = n % 10
    n = n // 10
    i = i * 10
    i = i + c
print(i)  
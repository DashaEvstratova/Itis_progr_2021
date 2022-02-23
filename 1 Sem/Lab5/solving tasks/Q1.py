a = float(input())
b = float(input())
c = float(input())
d = b**2 - 4*a*c
if a == 0:
    if b != 0:
        x = -c / b
        print('1', x)
    else:
        if c == 0:
            print(3)
        else:
            print(0)
if a != 0:
    if d == 0:
        x1 = (-b - (d)**0.5) / (2*a)
        print('1', x1)
    elif d > 0:
        x1 = (-b - (d)**0.5) / (2*a)
        x2 = (-b + (d)**0.5) / (2*a)
        if x1 > x2:
            print('2', x2, x1)
        else:
            print('2', x1, x2)
    else:
        print(0)
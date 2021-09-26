A = int(input())
B = int(input())
C = int(input())
if A > B:
	if A > C:
		print(A)
	else:
		print(C)
else:
	if C > B:
		print(C)
	else:
		print(B)

# 3 оператора (можно и обойтись без них)
'''
A = int(input())
B = int(input())
C = int(input())
e = A // B
e = ((e+2) // (e+1)) % 2
d = (e+1) % 2
max1 = A*e + B*d
e = max1 // C
e = ((e+2) // (e+1)) % 2
d = (e+1) % 2
print(max1*e + C*d)
'''
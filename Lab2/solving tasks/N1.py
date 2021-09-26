a = int(input())
b = int(input())
c = int(input())
count = 0
if a == b:
	count += 2
	if b == c:
		count +=1
elif b == c:
	count += 2
	if c == a:
		count +=1
elif a == c:
	count += 2
	if c == b:
		count +=1
print(count)
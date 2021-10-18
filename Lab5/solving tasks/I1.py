a = input()
if 'f' not in a:
	print(-2)
count = 0
for i in range(0, len(a)):
	if a[i] == 'f':
		count +=1
	if count == 2:
		print(i)
		break
if count == 1:
	print(-1)
n = int(input())
s = 0
c = 1
for i in range(1, n + 1): 
	c = c *i
	s = s + c
print(s)
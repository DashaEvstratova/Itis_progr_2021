def function():
	n = int(input())
	if n!=0:
		function()
		if (n**0.5) == int(n**0.5):
			global b 
			b = 1
			print(n, end=' ')
b = 0
function()
if b == 0:
	print(0)
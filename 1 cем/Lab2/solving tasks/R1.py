a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input()) 
b2 = int(input())
c2 = int(input())
# possible options with the same arrangement of boxes
first = (a1 // a2) * (b1 // b2) * (c1 // c2) 
second = (a1 // b2) * (b1 // a2) * (c1 // c2)
third = (a1 // c2) * (b1 // a2) * (c1 // b2)
fourth = (a1 // a2) * (b1 // c2) * (c1 // b2)
# selection of the greatest
if first >= second and first >= third and first >= fourth:
	print(first)
elif second >= first and second >= third and second >= fourth:
	print(second)
elif third >= second and third >= first and third >= fourth:
	print(third)
elif fourth >= second and fourth >= third and fourth >= first:
	print(fourth)
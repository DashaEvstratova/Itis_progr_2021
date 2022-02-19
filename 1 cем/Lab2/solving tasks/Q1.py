a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
if (a1 == a2 and b1 == b2 and c1 == c2) or (c1 == a2 and b1 == b2 and a1 == c2):
	print('Boxes are equal')
elif (b1 == a2 and a1 == b2 and c1 == c2) or (a1 == a2 and c1 == b2 and b1 == c2):
	print('Boxes are equal')
elif (a1 < a2 and b1 < b2 and c1 < c2) or (a1 < b2 and b1 < a2 and c1 < c2):
	print('The first box is smoller then the second one')
elif (c1 < a2 and a1 < b2 and b1 < c2) or (a1 < a2 and c1 < b2 and b1 < c2):
	print('The first box is smoller then the second one')
elif (c1 < a2 and b1 < b2 and a1 < c2) or (c1 < b2 and b1 < a2 and a1 < c2):
	print('The first box is smoller then the second one')
elif (a1 > a2 and b1 > b2 and c1 > c2) or (a1 > b2 and b1 > a2 and c1 > c2):
	print('The first box is larger then the second one')
elif (c1 > a2 and a1 > b2 and b1 > c2) or (a1 > a2 and c1 > b2 and b1 > c2):
	print('The first box is larger then the second one')
elif (c1 > a2 and b1 > b2 and a1 > c2) or (c1 > b2 and b1 > a2 and a1 > c2):
	print('The first box is larger then the second one')
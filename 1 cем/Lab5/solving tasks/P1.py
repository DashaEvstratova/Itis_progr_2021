a = input()
r = a.find('h')
l = a.rfind('h')
a1 = a[:(l)]
a1 = a1[(r+1):]
a1 = a1.replace('h', 'H')
print(a[:(r+1)] + a1 + a[l:])
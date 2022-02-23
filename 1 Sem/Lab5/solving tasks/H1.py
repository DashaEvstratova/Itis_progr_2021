a = input()
r = a.find('h')
l = a.rfind('h') + 1
a = a[:r] + a[l:]
print(a)
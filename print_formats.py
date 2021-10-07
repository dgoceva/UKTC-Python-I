import math

a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

p = a+b+c
print('P= ', p)
print('P= '+str(p))
print('P= {0}'.format(p))
print('P= %d' % (p))
print(f'P= {p}')

a = float(input('a= '))
b = float(input('b= '))
h = float(input('h= '))
s = (a+b)/2*h
print('S = '+str(s))

print(math.ceil(34.25))
print(math.floor(34.25))
print(round(23.54, 1))

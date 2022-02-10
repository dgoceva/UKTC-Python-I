import math

a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

d = b*b - 4*a*c
print(d)

if d == 0:
    x = -b/(2*a)
    print('x= ', x)
elif d > 0:
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print('x1= '+str(x1), 'x2= '+str(x2), sep='\n')
else:
    xr = -b/(2*a)
    xi = math.sqrt(math.fabs(d))
    print('x1= ' + str(xr)+'-i'+str(xi),
          'x2= '+str(xr)+'+i'+str(xi), sep='\n')

import numpy as np
import matplotlib.pyplot as plt
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

xplt = np.arange(-20, 20, 1)
yplt = a*xplt*xplt+b*xplt+c
plt.plot(xplt, yplt, color='indigo', label='y=ax**2+bx+c')
yplt = xplt**2
plt.plot(xplt, yplt, color='yellowgreen', label='y=x^2')
yplt1 = xplt*a+b
plt.plot(xplt, yplt1, color='cyan', label='y=ax+b')
plt.legend(loc='upper right', frameon=False)
plt.title('Графики на функции')
plt.xlabel('X')
plt.ylabel('Y', loc='top', rotation='horizontal')
plt.show()

# print('Hello Python!')
# print(3/2)

a = int(input('a='))
a = 5
print('S='+str(a*a))

num1, num2 = map(int, input('Input numbers: ').split(','))
print(num1, num2, num1+num2, sep=';')

name = input('Input name: ')
print('Hello '+name)

name = input('Name: ')
family = input('Family: ')
age = int(input('Age: '))
town = input('Town: ')

print('You are {0} {1}, {2} years old from {3}.'
      .format(name, family, age, town))

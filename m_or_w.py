sex = input('Sex[m/f]: ')
age = int(input('Age: '))

if sex == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Masters.')
elif sex == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')
else:
    print('Unknown')

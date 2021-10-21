amount = float(input('Amount = '))
money = input('Money = ')

if money == 'USD':
    print('USD {0} = {1} BGN'.format(amount, round(amount*1.79549, 2)))
elif money == 'EUR':
    print('EUR {0} = {1} BGN'.format(amount, round(amount*1.95583, 2)))
elif money == 'GBP':
    print('GBP {0} = {1} BGN'.format(amount, round(amount*2.53405, 2)))
else:
    print('Error')

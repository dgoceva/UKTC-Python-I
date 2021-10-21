amount = float(input('Amount = '))
money = input('Money = ')
output = input('Output = ')

result = amount
if money == 'USD':
    result *= 1.79549
elif money == 'EUR':
    result *= 1.95583
elif money == 'GBP':
    result *= 2.53405
elif money != 'BGN':
    print('Error')

if output == 'USD':
    result /= 1.79549
elif output == 'EUR':
    result /= 1.95583
elif output == 'GBP':
    result /= 2.53405
elif output != 'BGN':
    print('Error')

print('{2} {0} = {1} {3}'.format(amount, round(result, 2), money, output))

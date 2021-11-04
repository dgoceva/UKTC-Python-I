time1 = int(input('Input time for 1: '))
time2 = int(input('Input time for 2: '))
time3 = int(input('Input time for 3: '))

sum = time1 + time2 + time3
print('{0:d}:{1:02d}'.format(sum//60, sum % 60))

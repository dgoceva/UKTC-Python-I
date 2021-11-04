points = int(input('Input points: '))

bonus_points = 0
if points <= 100:
    bonus_points = 5
elif points > 1000:
    bonus_points = points*0.1
else:
    bonus_points = points*0.2

if points % 2 == 0:
    bonus_points += 1
elif points % 10 == 5:
    bonus_points += 2

print('All points: ', points+bonus_points, ' Bonus points: ', bonus_points)

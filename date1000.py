import datetime as dt

print(dt.datetime.now())

day = int(input('[1-31]: '))
month = int(input('1-12: '))
year = int(input('year: '))

#  1000 = 2 years + 9 months + 0 days

input_date = dt.datetime(year, month, day)
print(input_date)
print(input_date+dt.timedelta(days=1000))

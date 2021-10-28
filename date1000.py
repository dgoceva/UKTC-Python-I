import datetime as dt

str_date = input('Input date[dd-mm-yyyy]: ')
input_date = dt.datetime.strptime(str_date, '%d-%m-%Y')
out_date = input_date+dt.timedelta(days=1000)
print(out_date.strftime('%d-%m-%Y'))

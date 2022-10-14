import datetime
from datetime import timedelta

date_entry = input('Enter the Future date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
Future_date= datetime.date(year, month, day)
print(Future_date)
CurrentDate=datetime.date.today() 
print(CurrentDate)
delta = Future_date - CurrentDate
print(f'Difference is {delta.days} days')



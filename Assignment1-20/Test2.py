from datetime import datetime
Future_time = input('Enter the Future date in HH:MM:SS format')
t2 = datetime.strptime(Future_time, "%H:%M:%S")
print('Future time:', t2.time())
t1 = datetime.now() 
t1 = t1.strftime("%H:%M:%S")
t11 = datetime.strptime(t1, "%H:%M:%S")
print('Current time:', t11.time())
delta = t2 - t11
print(f'Difference in time is {delta}')

# import datetime
# from datetime import datetime
# from datetime import timedelta
# time = input('Enter the Future date in HH-MM-SS format')
# hours, mins, sec = map(int, time.split(':'))
# Ahead_time = datetime.datetime(hours, mins, sec)
# CurrentTime = datetime.now() 
# current_time = CurrentTime.strftime("%H:%M:%S")
# print(current_time)
# delta = Ahead_time - CurrentDate
# print(f'Difference is {delta.days} days')


# time = input("Enter time in HH:MM:SS\n")
# hour, min, sec = [int(i) for i in time.split(":")]
# if hour >= 24 or min > 60 or sec > 60 :
#     print("Invalid time")
#     exit()
# print("It is", hour, "hours", min, "minutes", sec, "seconds")
# Future_time = hour, min, sec
# print(hour, min, sec)
# print(type(Future_time))
# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# print(current_time)
# CurrentTime = datetime.now() 
# current_time = CurrentTime.strftime("%H:%M:%S")
# print(current_time)
# delta = Future_time - current_time
# print(f'Difference is {datetime.timedelta} time')
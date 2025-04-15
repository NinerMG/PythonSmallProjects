import datetime as dt

# can get current date and time


now = dt.datetime.now()
year = now.year
#print(year)
if year == 2024:
    print("Yes")

day_of_week = now.weekday()
#print(day_of_week)
#print(now)

date_of_birth = dt.datetime(year=1994 , month=1 , day=1)
print(date_of_birth)
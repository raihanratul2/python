from datetime import datetime, date, timedelta
# from dateutil.relativedelta import relativedelta
# DateN = date.today()
# print(f"Current date is: {DateN}")

# TimeN = datetime.now().time()
# print(f"Current time is: {TimeN}")

DateTN = datetime.now()
print(f"Current date and time is: {DateTN}\n")


# Date
dt_str = DateTN.strftime("%A %B %y")
print(f"Current Date Formated: {dt_str}")

dt_str = DateTN.strftime("%D : Day %w of week %a, %d, %b, %Y")
print(f"Current Date Formated2: {dt_str}")

dt_str = DateTN.strftime("%b %d %y")
print(f"Current Date Formated3: {dt_str}\n")

#times
dt_str = DateTN.strftime("%H:%M:%S - Hour:%H Minutes:%M Seconds:%S Microsecond:%f")
print(f"Current Time Formated: {dt_str}")

dt_str = DateTN.strftime("Bd time Now %I:%M %p")
print(f"Current Time Formated2: {dt_str}")

dt_str = DateTN.strftime("%b %d %y")
print(f"Current Time Formated3: {dt_str}")


#timedelta
aft_2yrs=DateTN + timedelta(days=30*2+365*2)

dt_str = aft_2yrs.strftime("%A %B %y")
print(f"after 2 days,month,year Date Formated: {dt_str}")

diff = aft_2yrs - DateTN
print(f"Diffrence Between now and 2years,months,days Date Formated:{diff}")

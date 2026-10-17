import datetime
now = datetime.datetime.now()
print(now)
print("welcome to the weather app")
print("today date is", now.strftime("%Y-%m-%d"))
print("current time is", now.strftime("%H:%M:%S"))
print("todays Weather")
city = input("Enter your city name: ")

temp = int(input("whats temperature right now? "))

if temp > 50:
    print("its too hot outside")
elif temp > 40:
    print("its hot outside")
elif temp > 30:
    print("its warm outside")
elif temp > 20:
    print("its cool outside")
else:
    print("write your temperature ")

print("thank you for using the weather app")

import calendar
print(calendar.calendar(now.year))

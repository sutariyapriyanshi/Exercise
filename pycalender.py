# Display calender in python
import calendar
y=int(input("Enter year:"))
m=int(input("Enter month:"))
d=int(input("Enter day0:"))

# c=calendar.month(y,m)
# print("\n",c)
# d=calendar.setfirstweekday(calendar.SUNDAY)
# print(d)
y1=int(input("Enter year:"))
y2=int(input("Enter year:"))

p=calendar.leapdays(y1, y2)
q=calendar.weekday(y, m, d)
print(p)
print(q)
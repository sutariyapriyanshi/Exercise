import datetime
today = datetime.datetime.now()
yesterday= today - datetime.timedelta(days=1)
print(today)
print(yesterday)

for i in range(0,7):
    print("The date and time is",today - datetime.timedelta(days=i))

# dates_list=[list[datetime.datetime.now()]]
# print(today)

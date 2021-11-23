import datetime

s = "2021-11-12"

dt = datetime.datetime.strptime(s, "%Y-%m-%d")
print(dt)

s = "2021-11-12 10:20:30"

dt = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(dt)

s = "10:20:30"

dt = datetime.datetime.strptime(s, "%H:%M:%S")
print(dt)

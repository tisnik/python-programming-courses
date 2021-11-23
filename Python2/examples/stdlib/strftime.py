import datetime

dt = datetime.datetime.now()
print(dt)

s = dt.strftime("%Y-%m-%d")
print(s)

s = dt.strftime("%d.%m.%Y")
print(s)

s = dt.strftime("%m/%d/%Y")
print(s)

s = dt.strftime("%H:%m:%S")
print(s)

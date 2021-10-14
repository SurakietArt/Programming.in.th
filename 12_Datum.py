import datetime
m, d = input().split()

x = datetime.datetime(2009, int(d), int(m))

print(x.strftime("%A"))
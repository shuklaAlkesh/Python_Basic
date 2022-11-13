import datetime

x= datetime.datetime.now()

print(x)

m = x.strftime("%y") # it returns a year  in short version
print(m)

m = x.strftime("%Y") # it returns a year  in long version
print(m)

m = x.strftime("%I") # it returns an hour  in (0-12)
print(m)

m = x.strftime("%m") # it returns a month
print(m)

m = x.strftime("%M") # it returns a minute in (0-59)
print(m)

m = x.strftime("%b") # it returns a month name  in short version
print(m)

m = x.strftime("%B") # it returns a month name  in full version
print(m)
m = x.strftime("%H") # it returns a hour  in (0-23)
print(m)

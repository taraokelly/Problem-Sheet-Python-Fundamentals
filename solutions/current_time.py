import datetime

now = datetime.datetime.now()

#print("Current date and time: " + str(now))

print("Current date and time: " + now.strftime("%Y-%m-%d %H:%M"))
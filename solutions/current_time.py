# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Python fundamentals
# 1. Write a program that prints the current time and date to the console.

# https://docs.python.org/3/library/datetime.html
import datetime

# Returns the current local date and time
now = datetime.datetime.now()

# strftime formats string based on args
print("Current date and time: " + now.strftime("%Y-%m-%d %H:%M"))
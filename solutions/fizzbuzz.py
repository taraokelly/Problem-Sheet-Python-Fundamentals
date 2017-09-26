# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Python fundamentals
# 3. Write a program that prints the numbers from 1 to 100, except for the following conditions. For multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# http://pythoncentral.io/pythons-range-function-explained/
for x in range(1,100+1):
    if (x % 3 == 0) & (x % 5 == 0):
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
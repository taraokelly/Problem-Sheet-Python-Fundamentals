# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Python fundamentals
# 9. Implement the square root function using Newton's method. In this case, Newton's method is to approximate sqrt(x) by picking a starting point z and then repeating:
#       z_next = z - ((z*z - x) / (2 * z))
# To begin with, just repeat that calculation 10 times and see how close you get to the answer for various values (1, 2, 3, ...). Next, change the loop condition to stop once the value has stopped changing (or only changes by a very small delta). How close are you to the math.sqrt value?

# https://docs.python.org/3/library/math.html
import math
# https://docs.python.org/2/library/decimal.html
from decimal import *

# Loop Newton's square root equation 10 times
def newton_square_root(x,z):
    d = 1
    while d > 0.0001:
        z_next = z - ((z*z-x)/(2*z))
        d = abs(z-z_next)
        z = z_next
    return z

# Get user input
x = Decimal(input("Enter x: "))
z = Decimal(input("Enter z: "))

# Calculate difference and print results
newton_res = newton_square_root(x,z)
res = Decimal(math.sqrt(x))
#https://stackoverflow.com/questions/13602170/how-do-i-find-the-difference-between-two-values-without-knowing-which-is-larger
diff = abs(newton_res-res) 
print("Newton Result:", newton_res)
print("Actual Result:", res)
print("Difference:", diff)
# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Python fundamentals
# 4. Write a function that calculates the sum of the digits of the factorial of a number. n! means n x (n − 1) ... x 3 x 2 x 1. For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27. Find the sum of the digits in the number 100!

n, sum = 100, 0;

# http://pythoncentral.io/pythons-range-function-explained/
for x in range(n,0,-1):
    if x == n:
        sum = n;
    else:
        sum = sum * x;

# Print factorial
print(sum)
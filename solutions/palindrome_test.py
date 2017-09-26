# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Python fundamentals
# 7. Write a function that tests whether a string is a palindrome.

# A palindrome is a sequence that reads the same backwards as forwards.


# Palindrome function 
# Use of extended slices by putting negative one as a step reverses the indices
# https://docs.python.org/2.3/whatsnew/section-slices.html
def palindrome_test(seq):
    return seq[::-1] == seq

# Get user input, test input and print result
seq = input('Palindrome Test.\nEnter sequence: ')
print('Is ['+seq+'] a palindrome:', palindrome_test(seq))
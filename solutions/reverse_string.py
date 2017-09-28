# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Python fundamentals
# 10. Write a function to reverse a string.

# This is how I would have implemented the function in a real life scenario
def rev_string_extended_slices(old_string):
    return old_string[::-1]

# However, to actually implement this as a hard coded function:
def reverse_string_manually(old_string):
    new_string = []
    index = len(old_string)
    while index:
        index -= 1                       
        new_string.append(old_string[index])
        # https://www.tutorialspoint.com/python/string_join.htm
    return ''.join(new_string)

# Get input print results
string = input("Enter String you wish to be reversed:\n")

# Print reversed string
print(rev_string_extended_slices(string))
print(reverse_string_manually(string))
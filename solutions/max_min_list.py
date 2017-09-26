# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Python fundamentals
# 6. Write a function that returns the largest and smallest elements in a list.

user_list = []

# get user input
n = int(input('How many numbers: '))
for x in range(n):
    numbers = int(input('Enter number: \n'))
    user_list.append(numbers)

# use min and max functions
# https://docs.python.org/3/library/functions.html#max
# https://docs.python.org/3/library/functions.html#min
print("Largest element in the list is :", max(user_list), "\nSmallest element in the list is :", min(user_list))
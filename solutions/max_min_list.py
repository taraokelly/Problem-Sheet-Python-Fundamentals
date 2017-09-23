user_list = []
# get user input and analyse use min and max functions
n = int(input('How many numbers: '))
for x in range(n):
    numbers = int(input('Enter number: \n'))
    user_list.append(numbers)
print("Largest element in the list is :", max(user_list), "\nSmallest element in the list is :", min(user_list))
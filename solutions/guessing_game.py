# Tara O'Kelly - G00322214
# Emerging Technologies, Year 4, Software Development, GMIT.

# Problem set: Python fundamentals
# 5. Write a guessing game where the user must guess a secret number. After every guess the program tells the user whether their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they input the same number multiple times consecutively.

# https://docs.python.org/3/library/random.html
from random import randint

# Returns a random integer n such that 1 <= n <= 10
n = randint(1, 10)
x, correct, guess_cnt, incorrect_inputs = 0, 0, 0, []

# Get user input, analyse input until correct answer is quessed
while correct == 0:
    x = input("Enter a number: ")
    
    if int(x) == n:
        correct = 1;
    elif int(x) < n:
        print("Too small");
        if int(x) not in incorrect_inputs:
            incorrect_inputs.append(int(x));
            guess_cnt+=1;
    elif int(x) > n:
        print("Too large");
        if int(x) not in incorrect_inputs:
            incorrect_inputs.append(int(x));
            guess_cnt+=1;

# Print results
print("Congrats! The answer was "+ str(n) + ".")
if incorrect_inputs:
    print("Incorrect Guesses: " + str(guess_cnt))
    print(incorrect_inputs)
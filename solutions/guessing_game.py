from random import randint

n = randint(1, 10)
x = 0
incorrect_inputs = []
correct = 0;
guess_cnt = 0;

#get user input, analyse input and print result

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

print("Congrats! The answer was "+ str(n) + ".")
print("Incorrect Guesses: " + str(guess_cnt))
print(incorrect_inputs)
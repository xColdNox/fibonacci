from time import *

# I tried to create Fibonacci sequence that asks for input repeatedly.
# First we ask for a number to calculate Fibonacci sequence and make sure it's a number.

while True:
    user_number1 = input("How long do you want the Fibonacci sequence to be? Enter a number: ")
    try:
        n1 = int(user_number1)
        break
    except ValueError:
        print("It has to be a number!")

# Further, we check if it's not a negative value.

while n1 < 0:
    print("Invalid number!\n")
    user_number1 = input("Try again, positive value this time: ")
    n1 = int(user_number1)
print("You got it! Here comes the Fibonacci sequence:")
    
# Then we define the Fibonacci sequence.

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Please enter a positive number!\n")
    elif n == 0:
        return a
    elif n == 1 or n == 2:
        return b
    else:
        for i in range(1,n):
            c = a + b
            a = b
            b = c
        return c

# We print out the result.

for n in range(n1):
    print(fibonacci(n))

# We proceed to the step where it will continously ask us if we want to calculate another Fibonacci sequence.

while True:
    user_number2 = input("There you go. Do you want to try another number? Enter (yes/no): ")
    if (user_number2 != "yes") and (user_number2 != "no"):
        print("Invalid answer, please enter 'yes' or 'no'.")
    elif user_number2 == "no":
        print("Ok, glad I could help!")
        sleep(4)
        break
    elif user_number2 == "yes":
        while True:
            user_number2 = input("Ok! Please enter a desired length: ")
            try:
                n2 = int(user_number2)
                break
            except ValueError:
                print("It has to be a number!")            

        while n2 < 0:
            print("Invalid number!\n")
            n2 = int(input("Try again, positive value this time: "))
        print("You got it! Here comes the Fibonacci sequence:")
        for n in range(n2):
            print(fibonacci(n))

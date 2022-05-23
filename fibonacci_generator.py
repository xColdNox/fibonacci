import time


def get_number():
    """
    Function that asks the user for an integer and validates that it is a positive number.
    :return: validated user input
    :rtype: int
    """
    while True:
        user_number = input("How long do you want the Fibonacci sequence to be? Enter a number: ")
        try:
            n = int(user_number)

            # Further, we check if it's not a negative value.
            if n < 1:
                print("Number must be positive.\n")
            else:
                break
        except ValueError:
            print("It has to be a number!\n")
    return n


def fibonacci(n):
    """
    Generates and returns a fibonacci sequence.
    :param n: positive integer defining sequence length
    :return: fibonacci sequence list
    :rtype: list
    """
    # Then we define the Fibonacci sequence.
    sequence = [0, 1]
    if n < 3:
        return sequence[:n]
    for i in range(n-2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def ask_for_more():
    """
    Asks user if wants to continue.
    :return: True for "yes" and False for "no"
    :rtype: bool
    """
    while True:
        answer = input("There you go. Do you want to try another number? Enter (yes/no): ")
        if answer not in ["yes", "no"]:
            print("Invalid answer, please enter 'yes' or 'no'.\n")
        elif answer == "no":
            print("Ok, glad I could help!")
            time.sleep(4)
            return False
        elif answer == "yes":
            return True


if __name__ == "__main__":
    n = get_number()
    print(fibonacci(n))

    while ask_for_more():
        n = get_number()
        print(fibonacci(n))

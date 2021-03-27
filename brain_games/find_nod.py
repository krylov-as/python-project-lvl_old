"""Print 'Yes' if user right"""


import random


def gcd(first_number, second_number):
    """Find GCD two number."""
    if first_number == 0 or second_number == 0:
        return max(first_number, second_number)
    if first_number > second_number:
        return gcd(first_number - second_number, second_number)
    else:
        return gcd(first_number, second_number - first_number)


def game():
    """Check if the user has correctly identified a GCD two number.
    Repeat three times.
    """

    repeat = 0
    while repeat < 3:
        first_number = random.randint(1, 20)
        second_number = random.randint(1, 20)
        print('Question: {} {}'.format(first_number, second_number))
        user_answer = int(input())
        result_gcd = gcd(first_number, second_number)
        if result_gcd == user_answer:
            print('Correct!')
            repeat += 1
            if repeat == 3:
                return True
        else:
            wrong_output = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(wrong_output.format(user_answer, result_gcd))
            return False

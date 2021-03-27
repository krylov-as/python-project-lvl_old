"""Check rundom number is prime. Print correct unswer if true."""

import random


def is_prime(number):
    """Returns 'yes' if number is prime, else returns 'no'."""

    if number % 2 == 0:
        return 'Yes'
    devider = 3
    while devider * devider <= number and number % devider != 0:
        devider += 2
    return 'yes' if devider * devider > number else 'no'


def game():
    """Check if the user has correctly identified a prime number.
    Repeat three times.
    """

    repeat = 0
    while repeat < 3:
        number = random.randint(1, 50)
        print('Question: {}'.format(number))
        check_number_is_prime = is_prime(number)
        user_answer = input()
        if (check_number_is_prime == user_answer):
            print('Correct!')
            repeat += 1
            if repeat == 3:
                return True
        else:
            wrong_text = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(wrong_text.format(user_answer, check_number_is_prime))
            return False

"""Checks three times if the user has correctly identified a prime number."""

import random


def is_even(number):
    """Return 'yes' if number is even, else return 'no'."""
    if number % 2 == 0:
        return 'yes'
    return 'no'


def game():
    """Check if the user has correctly identified a even number.
        Repeat three times.
    """
    repeat = 0
    while repeat < 3:
        uper_bound_rundom = 50
        number = random.randint(1, uper_bound_rundom)
        print('Question: {}'.format(number))
        check_number_is_even = is_even(number)
        user_answer = input()
        if (check_number_is_even == user_answer):
            print('Correct!')
            repeat += 1
        else:
            wrong_answer = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(wrong_answer.format(user_answer, check_number_is_even))
            repeat = 3

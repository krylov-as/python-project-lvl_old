"""Print 'Yes' if user right"""
import random

def is_even(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'


def game():
    for index in range(3):
        number = random.randint(1, 20)
        print("Question: {}".format(number))
        check_number_is_even = is_even(number)
        user_answer = input()
        if (check_number_is_even == user_answer):
            print("Correct!")
        else: 
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, check_number_is_even))
            break
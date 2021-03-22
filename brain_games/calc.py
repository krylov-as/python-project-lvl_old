"""Print 'Yes' if user right"""
import random


def game():
    for index in range(3):
        first_number = random.randint(1, 20)
        second_number = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            result = first_number + second_number
        elif operation == '-':
            result = first_number - second_number
        else:
            result = first_number * second_number
        print('{} {} {}'.format(first_number, operation, second_number))
        user_answer = int(input())
        if result == user_answer:
            print("Correct!")
        else: 
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, result))
            break
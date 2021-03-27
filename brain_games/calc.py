"""Print 'Yes' if user right."""
import random


def game():
    """Check result expression. Print Correct if result true."""
    repeat = 0
    while repeat < 3:
        upper_bound_rundom = 50
        first_number = random.randint(1, upper_bound_rundom)
        second_number = random.randint(1, upper_bound_rundom)
        operation = random.choice(['+', '-', '*'])
        if operation == '+':
            result_expression = first_number + second_number
        elif operation == '-':
            result_expression = first_number - second_number
        else:
            result_expression = first_number * second_number
        print('Question: {} {} {}'.format(first_number, operation, second_number))
        user_answer = int(input())
        if result_expression == user_answer:
            print('Correct!')
            repeat += 1
            if repeat == 3:
                return True
        else:
            text_wrong = "'{}' is wrong answer ;(. Correct answer was '{}'"
            print(text_wrong.format(user_answer, result_expression))
            return False

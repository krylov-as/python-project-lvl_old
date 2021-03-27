"""Сheck the correctness of guessing the missing number three times."""

import random


def game():
    """Check the correctness of guessing the missing number three times."""

    repeat = 0
    while repeat < 3:
        step = random.randint(1, 5)
        start = random.randint(1, 20)
        number_element = random.randint(5, 10)
        arifm_progr = []
        for index in range(number_element):
            arifm_progr.append(start + step * index)
        number_miss_element = random.randint(0, number_element - 1)
        miss_element = arifm_progr[number_miss_element]
        print('Question:', end=' ')
        print(*arifm_progr[0:number_miss_element], end=' ')
        print('..', end=' ')
        print(*arifm_progr[number_miss_element + 1:number_element])
        user_answer = int(input())
        if miss_element == user_answer:
            print('Correct!')
            repeat += 1
            if repeat == 3:
                return True
        else:
            wrong_output = "'{}' is wrong answer ;(. Correct answer was '{}'."
            print(wrong_output.format(user_answer, miss_element))
            return False

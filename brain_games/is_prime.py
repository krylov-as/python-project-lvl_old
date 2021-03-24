"""Check rundom number is prime. Print correct unswer if true"""
import random

def is_prime(n):
    if n % 2 == 0:
        return 'no'
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return 'yes' if d * d > n else 'no'


def game():
    for index in range(3):
        number = random.randint(1, 50)
        print("Question: {}".format(number))
        check_number_is_prime = is_prime(number)
        user_answer = input()
        if (check_number_is_prime == user_answer):
            print("Correct!")
        else: 
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, check_number_is_prime))
            break

"""Print 'Yes' if user right"""
import random
def gcd(first_number, second_number):
    if first_number == 0 or second_number == 0: 
         return max(first_number, second_number)
    if  first_number > second_number:
        return gcd(first_number - second_number, second_number)
    else:
        return gcd(first_number, second_number - first_number)


def game():
    for index in range(3):
        first_number = random.randint(1, 20)
        second_number = random.randint(1, 20)
        print('{} {}'.format(first_number, second_number))
        user_answer = int(input())
        result = gcd(first_number, second_number)
        if result == user_answer:
            print("Correct!")
        else: 
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, result))
            break

"""Print 'Yes' if user right"""
import random
def game():
    for i in range(3):
        step = random.randint(1, 5)
        start = random.randint(1, 20)
        number_element = random.randint(5, 10)
        arifm_progr  = []
        for index in range(number_element):
            arifm_progr.append(start + step * index)
        miss_element = random.randint(0, number_element-1)
        result = arifm_progr[miss_element]
        print(*arifm_progr[0:miss_element], '..', end=' ')
        print(*arifm_progr[miss_element+1:number_element])
        user_answer = int(input())
        if result == user_answer:
            print("Correct!")
        else: 
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(user_answer, result))
            break
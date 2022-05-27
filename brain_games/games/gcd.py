import random

question = 'What is the result of the expression?'


def make_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    for i in range(number_1):
        if number_2 % i == 0 and number_1 % i == 0:
            answer = i
    number = '{0} {1}'.format(number_1, number_2)
    return number, answer

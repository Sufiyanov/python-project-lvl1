import random

question = 'Find the greatest common divisor of given numbers.'


def make_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    for i in range(1, number_1 + 1):
        if number_2 % i == 0 and number_1 % i == 0:
            answer = str(i)
    number = '{0} {1}'.format(number_1, number_2)
    return number, answer

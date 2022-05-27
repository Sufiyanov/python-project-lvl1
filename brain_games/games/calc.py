import random

question = 'What is the result of the expression?'


def make_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        number = '{0} + {1}'.format(number_1, number_2)
        answer = str(number_1 + number_2)
    if operation == '-':
        number = '{0} - {1}'.format(number_1, number_2)
        answer = str(number_1 - number_2)
    if operation == '*':
        number = '{0} * {1}'.format(number_1, number_2)
        answer = str(number_1 * number_2)
    return number, answer

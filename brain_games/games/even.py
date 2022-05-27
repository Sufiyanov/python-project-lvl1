import random

question = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_answer():
    number = random.randint(1, 100)
    if number % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer

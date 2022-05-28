import random

question = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def make_answer():
    number = random.randint(1, 100)
    divider = []
    for i in range(1, number + 1):
        if number % i == 0:
            divider.append(i)
    if divider == 2:
        answer = 'yes'
    else:
        answer = 'no'
    return number, answer

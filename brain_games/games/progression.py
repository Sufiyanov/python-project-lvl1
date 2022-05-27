import random

question = 'What number is missing in the progression?'


def make_answer():
    number_position = random.randint(1, 100)
    number_progression = random.randint(1, 20)
    list_progression = [number_position]
    for i in range(10):
        list_progression.append(list_progression[-1] + number_progression)
    answer = random.choice(list_progression)
    list_progression[list_progression.index(answer)] = '...'
    number = list_progression
    return number, str(answer)

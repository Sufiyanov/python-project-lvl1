import prompt

max_round = 3


def run_game(game_name):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
    print(game_name.question)
    game_round = 0
    while game_round < max_round:
        number, correct_answer = game_name.make_answer()
        print('Question:', number)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            game_round += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            break
    if game_round == max_round:
        print('Congratulations, {0}!'.format(name))
    else:
        print("Let's try again, {0}!".format(name))

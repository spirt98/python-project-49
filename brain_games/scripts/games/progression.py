from random import randint
from games.body_games import game


def generate_question():
    startNumber = randint(1, 10)
    step = randint(1, 10)
    hiddenIndex = randint(0, 9)

    progression = [startNumber + step * i for i in range(10)]

    correctAnswer = str(progression[hiddenIndex])
    progression[hiddenIndex] = '..'

    question = ' '.join(map(str, progression))

    return question, correctAnswer


def game_progression():
    welcomeGame = 'What number is missing in the progression?'

    game(generate_question, welcomeGame)

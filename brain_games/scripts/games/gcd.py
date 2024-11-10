from random import randint
from games.body_games import game
from math import gcd


def generate_question():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    question = f'{number1} {number2}'
    correctAnswer = str(gcd(number1, number2))

    return question, correctAnswer


def game_gcd():
    welcomeGame = 'Find the greatest common divisor of given numbers.'

    game(generate_question, welcomeGame)

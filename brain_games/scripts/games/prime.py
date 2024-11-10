from random import randint
from games.body_games import game


def isPrime(number):
    if number % 2 == 0 or number == 1:
        return False
    divisor = 3
    while divisor * divisor <= number and number % divisor != 0:
        divisor += 2
    return divisor * divisor > number


def generate_question():
    number = randint(1, 100)

    question = str(number)
    correctAnswer = 'yes' if isPrime(number) else 'no'

    return question, correctAnswer


def game_prime():
    welcomeGame = ('Answer "yes" if given number is prime. '
                   'Otherwise answer "no".')

    game(generate_question, welcomeGame)

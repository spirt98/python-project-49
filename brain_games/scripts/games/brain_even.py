from random import randint
from body_game import game


def generate_question():
    number = randint(1, 1000)

    correctAnswer = 'yes' if number % 2 == 0 else 'no'

    return number, correctAnswer


def game_even():
    welcomeGame = 'Answer "yes" if the number is even, otherwise answer "no".'

    game(generate_question, welcomeGame)


def main():
    game_even()


if __name__ == "__main__":
    main()

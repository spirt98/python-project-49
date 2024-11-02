from random import randint
from body_game import game


def calc(number1: int, number2: int, operator: str):
    match operator:
        case '*':
            return number1 * number2
        case '+':
            return number1 + number2
        case '-':
            return number1 - number2
        case _:
            return 0


def generate_question():
    operators = ['*', '+', '-']

    number1 = randint(1, 20)
    number2 = randint(1, 20)
    operator = operators[randint(0, 2)]

    question = f'{number1} {operator} {number2}'
    correctAnswer = str(calc(number1, number2, operator))

    return question, correctAnswer


def game_calc():
    welcome_game = 'What is the result of the expression?'

    game(generate_question, welcome_game)


def main():
    game_calc()


if __name__ == "__main__":
    main()

import prompt
from random import randint


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def game_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')

    successAnswer = 0
    REQUIRED_ANSWER = 3

    while REQUIRED_ANSWER != successAnswer:
        number = randint(1, 1000)
        print(f'Question: {number}')

        userAnswer = prompt.string('Your answer: ')
        correctAnswer = 'yes' if number % 2 == 0 else 'no'

        if userAnswer != correctAnswer:
            print(f"'{userAnswer}' is wrong answer ;(. "
                  f"Correct answer was '{correctAnswer}'.")
            return 1
        else:
            print('Correct!')
            successAnswer += 1
    return 0


def main():
    name = welcome_user()

    result = game_even()

    if result == 0:
        print(f"Congratulations, {name}!")
    else:
        print(f"Let's try again, {name}!")


if __name__ == "__main__":
    main()

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def question_user(question):
    print(f'Question: {question}')
    answerUser = prompt.string('Your answer: ')
    return answerUser

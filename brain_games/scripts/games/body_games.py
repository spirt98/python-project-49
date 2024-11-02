from games.user_dialogs.user import welcome_user, question_user


def game(generate_question, welcomeGame):
    nameUser = welcome_user()

    print(welcomeGame)

    successAnswer = 0
    REQUIRED_ANSWER = 3
    while REQUIRED_ANSWER != successAnswer:
        question, correctAnswer = generate_question()

        answerUser = question_user(question)

        if answerUser != correctAnswer:
            print(f"'{answerUser}' is wrong answer ;(. "
                  f"Correct answer was '{correctAnswer}'.")
            print(f"Let's try again, {nameUser}!")
            return 0
        else:
            print('Correct!')
            successAnswer += 1

    print(f"Congratulations, {nameUser}!")

    return 0

# for qns dictionary is used
# where key=qn and value=ans
questions = {
    "1)Who created python?: ": "A",
    "2)Which year python was crated?: ": "B",
    "3)Python is tributes to which comedy group?: ": "C",
    "4)Is earth round?: ": "A"
}

# and for options list 2D lists are used
options = [["A. Guido Van Rossum", "B. Elon Musk", "C. Mahatma Gandhi", "D. Tony Stark"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2018"],
           ["A. Lonely Island", "B. Smooch", "C. Monty python", "Friends"],
           ["A. Yeah", "B. Nah!", "C. Sometimes", "D. What's Earth?"]]


# ------------------------
def guess_value() -> str:
    option = ["A", "B", "C", "D"]
    guessed_value = None
    while guessed_value not in option:
        guessed_value = input('Answer[A, B, C, D]? : ').upper()
    return guessed_value


# ------------------------
def check_answer(answer, guess) -> int:
    if answer == guess:
        print('CORRECT:)')
        return 1
    else:
        print('WRONG:(')
        return 0


# ------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for question in questions:
        print(question)
        for option in options[question_num - 1]:
            print(option)

        guess = guess_value()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(question), guess)
        question_num += 1
        print()

    display_score(correct_guesses, guesses)


# ------------------------
def display_score(correct_guesses, guesses):
    print('\n===============')
    print('  --RESULTS--')
    print('===============')

    print('Answers: ', end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print('guesses: ', end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    percentage = int((correct_guesses / len(questions)) * 100)
    print('percentage is : ', percentage, '%')


# ------------------------
def play_again() -> bool:
    response = input('Do you wanna play again?(Y/N): ').lower()
    if response == 'y':
        return True
    else:
        return False


# ------------------------
if __name__ == '__main__':
    new_game()

    while play_again():
        new_game()
    print('Bye!')

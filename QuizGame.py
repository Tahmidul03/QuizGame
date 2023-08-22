def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Please Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):

    if answer == guess:
        print("That is Correct")
        return 1
    else:
        print("That is incorrect")
        return 0


def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("Here are the results")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Here is your score: "+str(score)+"%")


def play_again():

    print("--------------------------------")
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
 "What is my Nickname?: ": "A",
 "How old am I?: ": "B",
 "What School I go to?: ": "C",
 "How many College friends I got?: ": "C"
}

options = [["A. Tommy", "B. Haque", "C. T", "D. I never have my own Nickname"],
          ["A. 20", "B. 21", "C. 18", "D. 19"],
          ["A. Queens College", "B. Queensborough College", "C. St Johns University"
           , "D. York College"],
          ["A. 8","B. 9", "C. 10", "D. 11"]]


new_game()

while play_again():
    new_game()

print("Have a Good One")

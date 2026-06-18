# import random
import random
user_attempts = 3
# Function for difficulty level
def user_difficulty():
    while True:
        try:
            # Prompt the user for difficulty level. "Enter Level: 1, 2, 3". If input not 1, 2, or 3, prompt again.
            user_level = int(input("Enter level: 1, 2, 3: "))
            if user_level > 3 or user_level < 0:
                print("ERROR: Invalid Input")
                continue
            break
        except:
            print("ERROR: Invalid Input")

    return user_level

# Function for number of questions
def user_questions():
    while True:
        try:
            # Prompt the user for number of questions to ask "Enter number of questions to ask: 3 to 10:". If input not <3 or > 10, prompt again.
            number_of_questions = int(input("Enter number of questions to ask: 3 - 10: "))
            if number_of_questions < 3 and number_of_questions > 10:
                print("ERROR: Please enter a number between 3 - 10")
                continue
            break
        except:
            print("Invalid Input")
    return number_of_questions


# If user_level = 1, X and Y should be 1 digit, non-negative, (0 - 9).
# If user_level = 2, X and Y should be 2 digit, non-negative, (10 - 99).
# If user_level = 3, X and Y should be 3 digit, non-negative, (100 - 999).
def main():
    random_generator = random.Random()
    number_of_questions = user_questions()
    user_difficulty_level = user_difficulty()
    number_of_tries = 3
    number_of_correct_answers = 0
    for question_number in range(number_of_questions):
        if user_difficulty_level == 1:
            X = random_generator.randint(0, 9)
            Y = random_generator.randint(0, 9)
        elif user_difficulty_level == 2:
            X = random_generator.randint(10, 99)
            Y = random_generator.randint(10, 99)
        elif user_difficulty_level == 3:
            X = random_generator.randint(100, 999)
            Y = random_generator.randint(100, 999)

        # prompt the user to solve each problem.
        right_answer = X + Y
        
        while True:
            try:
                user_input = int(input(f"{X} + {Y} = "))
                # If answer is correct, output CORRECT!!! prompt user to answer next question.
                if user_input == right_answer:
                    print("CORRECT!!\n")
                    number_of_correct_answers = number_of_correct_answers + 1
                    break
                else:
                    print("WRONG!!\n")
                    number_of_tries = number_of_tries - 1
            except:
                # If answer is not correct, output WRONG!!! prompt the user again, user has three tries in total to answer the question.
                print("WRONG!!\n")
                number_of_tries = number_of_tries - 1

            # If input not correct after three tries, output correct answer, prompt the user to answer the next question.
            if number_of_tries == 0:
                print(f"\nCorrect Answer: {X} + {Y} = {right_answer}")
                break 
    grade = number_of_correct_answers / number_of_questions
    user_score = grade * 100
    print(f"You got {number_of_correct_answers} out of {number_of_questions} questions correct: {user_score}% ")
main()
 


# The program should output user score and the percentage (formatted to 2 decimal places) correct.

# End the program

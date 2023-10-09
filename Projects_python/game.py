#Quize Game
# Define a list of questions
questions = (
    "What is the capital of France?",
    "What is the result of 8 x 7?",
    "Which planet is known as the 'Red Planet'?",
    "What is the past tense of the verb \"swim\"?",
    "Which ocean is the largest in the world?",
)

# Define a list of options for each question
options = (
    ("A. Paris", "B. London", "C. Berlin", "D. Rome"),
    ("A. 56", "B. 64", "C. 48", "D. 42"),
    ("A. Earth", "B. Mars", "C. Venus", "D. Jupiter"),
    ("A. Swimming", "B. Swam", "C. Swum", "D. Swimmed"),
    ("A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"),
)

# Define the correct answers
answers = ("A", "A", "B", "B", "D")

# Create empty lists to store user guesses and initialize score and question number
guesses = []
score = 0
question_num = 0

# Iterate through each question
for question in questions:
    print("-------------------------")
    print(question)

    # Print the options for the current question
    for option in options[question_num]:
        print(option)

    # Prompt the user for their guess and convert it to uppercase
    guess = input("Enter (A, B, C, D) : ").upper()
    guesses.append(guess)

    # Check if the guess is correct and update the score accordingly
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")

    # Move on to the next question
    question_num += 1

print("-------------------------")
resultt = "---RESULT---"
print(resultt.center(50))

# Print the correct answers
print("Answers :", end="")
for answer in answers:
    print(answer, end=" ")
print()

# Print the user's guesses
print("Guesses :", end="")
for guess in guesses:
    print(guess, end=" ")
print()

# Calculate and print the user's score as a percentage
result = int(score / len(questions) * 100)
print(f"You'r score is : {result} %")

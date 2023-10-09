import random

while True:
    # Define the choices for the game
    choices = ["rock", "paper", "scissors"]
    # Computer randomly selects a choice
    computer = random.choice(choices)
    player = None
    # Ask the player for their choice and validate it
    while player not in choices:
        player = input("Rock, Paper, Scissors: ").lower()
    # Display a separator for clarity
    print("--------------------")  
    print("Player: " + player)
    print("Computer: " + computer)
    print("--------------------")
     # Determine the winner of the round
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")
          
    # Ask if the user wants to play again by using a while loop
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        break
      
print("Bye! :( ")

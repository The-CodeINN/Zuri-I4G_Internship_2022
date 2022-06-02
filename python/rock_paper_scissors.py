# Program for a rock-paper-scissors game

import random

input("Welcome to Rock, Paper, Scissors! Press Enter to continue...\n")

user_score = 0
CPU_score = 0

# Available choices
choice_list = ["R", "P", "S"]

# Game loop
while True:
# User input and CPU input with validation

    # Randomize CPU choice
    random_index = random.randint(0, 2)
    CPU_choice = choice_list[random_index]
    
    # User input
    user_choice = input(
        "Choose R for Rock, P for Paper, or S for Scissors: \n").upper()
    
    # Checking if user input is valid
    while user_choice not in choice_list:
        user_choice = input(
            "That is not a valid choice. Please try again: \n").upper()

    print(f"CPU : {CPU_choice}, Player : {user_choice}\n")

# Game logic
    while user_choice == CPU_choice:
        print("It's a tie!\n")
        user_choice = input("Please choose again: \n").upper()
        while user_choice not in choice_list:
            user_choice = input(
                "That is not a valid choice. Please try again: \n").upper()
        print(f"CPU : {CPU_choice}, Player : {user_choice}\n")
        break
    if user_choice == "R":
        if CPU_choice == "S":
            print("You win!\n")
            user_score += 1
        else:
            print("You lose!\n")
            CPU_score += 1
    elif user_choice == "P":
        if CPU_choice == "R":
            print("You win!\n")
            user_score += 1
        else:
            print("You lose!\n")
            CPU_score += 1
    elif user_choice == "S":
        if CPU_choice == "P":
            print("You win!\n")
            user_score += 1
        else:
            print("You lose!\n")
            CPU_score += 1

# Final score
    print(f"Player score is {user_score} and the CPU score is {CPU_score}\n")

# Play again?
    repeat_choice = input("Would you like to play again? (Y/N): \n").upper()
    while repeat_choice not in ["Y", "N"]:
        repeat_choice = input(
            "That is not a valid choice. Please try again: \n").upper()

    if repeat_choice == "N":
        break
    
# End of game
print(
    f"Thanks for playing! Final score is Player: {user_score} and CPU: {CPU_score}")

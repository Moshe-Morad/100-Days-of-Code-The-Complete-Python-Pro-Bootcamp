from random import randint
from art import logo


# Number Guessing Game Objectives:
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        turns = 10
        return turns
    else:
        turns = 5
        return turns


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = randint(1, 100)
    print(f"Pssst, the correct answer is {random_number}")
    user_guess = -1

    lives = set_difficulty()
    print(f"You have {lives} attempts remaining to guess the number.")

    while lives != 0 and user_guess != random_number:
        user_guess = int(input("Make a guess: "))
        if user_guess > random_number:
            print("Too high")
            lives -= 1
        elif user_guess < random_number:
            print("Too low")
            lives -= 1
        if user_guess == random_number:
            print(f"You got it! The answer  was {random_number}.")
        if lives == 0:
            print("You've run out of guesses, you lose.")
        elif lives > 0 and user_guess != random_number:
            print(f"You have {lives} attempts remaining to guess the number.")
            print("Guess again.")


game()

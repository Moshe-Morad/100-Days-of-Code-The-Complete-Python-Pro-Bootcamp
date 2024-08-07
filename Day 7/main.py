import random
from hangman_art import logo
from hangman_art import stages
from hangman_words import word_list


def game():
    print(logo)
    end_of_game = False
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6

    # Testing code
    print(f'Pssst, the solution is {chosen_word}.')

    # Create blanks
    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("you lose")
        print(stages[lives])

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

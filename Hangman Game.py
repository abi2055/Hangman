import random

# Reads a list of hangman words from a text file and reformats
with open ("C:\Programming Files\words.txt") as file:
    words = file.read().splitlines()

# Function returns a random word from the file
def get_word():
    secret_word = random.choice(words).lower()
    return secret_word

# Function serves as a starting screen for users
def start():
    lives = 0
    while True:
        choice = input("""Welcome to Hangman!
Play or Quit? """).lower()
        if choice == "play":
            while True:
                mode = input("""Choose Difficulty!
Easy - 10 lives
Moderate - 8 Lives
Hard - 6 lives
Mode: """).lower()
                if mode == "easy":
                    lives = 10
                    return lives
                    break
                elif mode == "moderate":
                    lives = 8
                    return lives
                    break
                elif mode == "hard":
                    lives = 6
                    return lives
                    break
                else:
                    print("Please Select a Valid Mode!")
            print(f"You chose {mode} mode ({lives} lives)")
        elif choice == "quit":
            print("The Game Will now terminate! Come again Soon!")
            return -1
            break
        else:
            print("Please Enter a Valid Command, Try Again!")
# Goes through and determines the amount of a lives a user will have and return the number of lives
# to be manipulated by the rest of the program
# exception handling included

# Function starts the game, parameters x and y are for the number of lives (x) and the generated secret word (y)
def game(x, y):
    hearts = x
    print(f"Number of lives {hearts}")
    guess_word = y
    # stores the secret word
    letter_list = []
    # list of letters that user already inputted
    length_word = len(guess_word) * "_"
    list_word = list(guess_word)
    # converts the secret word into a usable list
    temp_list = []
    # temporary list for list manipulation
    for blank in range(len(guess_word)):
        temp_list.append("_")
        # stores blanks
    print(length_word)
    while hearts != 0: # user decision tree
        decision = input("\nWould you like to guess a word or letter: ").lower()
        if decision == "letter":
            guess_letter = input("Guess a letter: ")
            if guess_letter in letter_list:
                print("You have already guessed that letter! Try Again!")
            elif guess_letter in guess_word:
                for x in range(len(guess_word)):
                    if guess_letter == list_word[x]:
                        del temp_list[x]
                        temp_list.insert(x, guess_letter)
                print("".join(temp_list))
                letter_list.append(guess_letter)
            else:
                print(f"Word does not consist of the letter {guess_letter}")
                hearts = hearts - 1
                print(f"Lives = {hearts}")
                letter_list.append(guess_letter)
        elif decision == "word":
            word_guess = input("What is your guess? ").lower()
            if word_guess == guess_word:
                print(f"Congrats! You Won! The word is {guess_word}")
                break
            else:
                print("That is not correct! Try again!")
                hearts = hearts - 1
                print(f"Lives = {hearts}")

    if hearts == 0:
        print("You lost! Try Again?")
        print(f"Tho the word was {guess_word}")

lives = 0
while True:
    lives = start()
    if lives == -1:
        break
    secret_word = get_word()
    game(lives, secret_word)

# Starts the game and loops through it as long as player does not quit









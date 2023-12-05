import random
#Choses a rondom word from the set array 
def choose_word():
    word_list = ["apple","barzin","luigi","mario"]
    return random.choice(word_list)
#Displays what letters you have already guessed 
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word
#ASCI drawing of the hangman 
def display_hangman(incorrect_attempts):
    hangman_art = [
        "   +---+\n   |   |\n       |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n       |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n   |   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|   |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n       |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  /    |\n       |\n=========",
        "   +---+\n   |   |\n   O   |\n  /|\\  |\n  / \\  |\n       |\n========="
    ]
    return hangman_art[incorrect_attempts]
#Game function
def hangman():
    #Member variables
    max_attempts = 6
    word_to_guess = choose_word()
    guessed = []
    incorrect_attempts = 0
    print("Welcome to Hangman Game")
    print(display_word(word_to_guess, guessed))
    #Looping menu 
    while True:
        guess = input("Guess a letter: ").lower()
        #User can only enter letters
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        #Checks if the user has already gussed the letter
        if guess in guessed:
            print("That letter has been guessed.")
            continue
        #Appends guess to array
        guessed.append(guess)
        #Incorrect geuss statment
        if guess not in word_to_guess:
            incorrect_attempts += 1
            print("Incorrect!")
            print(display_hangman(incorrect_attempts))
            print(f"Attempts remaining: {max_attempts - incorrect_attempts}")
            #Checks if user is out of attempts or not
            if incorrect_attempts >= max_attempts:
                print("You lost, The word was:", word_to_guess)
                break
        #Has to be correct otherwise
        else:
            print("Correct guess!")
        displayed = display_word(word_to_guess, guessed)
        print(displayed)
        #Checks to see if the user has won based on -
        if "_" not in displayed:
            print("You guessed the word!")
            print("Goodbye :)")
            break
#Main FUNC
if __name__ == "__main__":
    hangman()


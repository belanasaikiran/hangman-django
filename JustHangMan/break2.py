import random
words = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]

# The player should be allowed to guess incorrectly 1/2 the number of characters in the
# word. So for example if the selected word in "Pen", the player can make 2 incorrect
# guesses before loosing the game.

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
guessedLetters = []
game_word = random.choice(words).upper()
game_word_len = len(game_word)


def init():
    print("Welcome to Hangman! 🕴")
    # print(game_word)


def __main__():
    init()

    # print(game_word_len)
    print("Your Mission is to find the word for", game_word_len, "letters\n")
    Fill_Letters = game_word_len * "_"
    print(Fill_Letters)
    print("\nAvailable Letters: \n", alphabets)

    # The player should be allowed to guess incorrectly 1/2 the number of characters in the word.
    chances = game_word_len//2  # floor division

    while True:

        if(game_word_len < 4):
            chances = 3
            print("\nYou have", chances, "remaining chances left")
        else:
            print("\nYou have", chances, "remaining chances left")

        if chances == 0:
            print("Sorry, You ran out of chances")
            break


        if "_" in Fill_Letters:
            while True:
                option = input("Guess a letter: ").upper()

                if len(option) == 1:
                    # print(option)
                    guessedLetters.append(option)
                    print("Guessed Letters: ", guessedLetters)
                    break
                else:
                    print('Enter a single letter only')
                    continue

            if option in game_word:
                print("That's great," + option + " exists\n")
            else:
                print(option, "doesn't exist in word, try a different one \n")
                chances = chances - 1



            if (option in alphabets):
                    # print(option, "present in alphabets")
                    alphabets.remove(option)
                    print(alphabets)
            else:
                print("Please choose a letter from the available alphabets")
                print(alphabets)

            for i in range(game_word_len):
                if (option == game_word[i]):
                    Fill_list = list(Fill_Letters)
                    Fill_list[i] = option
                    Fill_Letters = ''.join(Fill_list)
                    # print(Fill_Letters)

            print("\n", Fill_Letters)

            continue
        else:
            print("You Win! 🥳 🎉")
            break


# Execute main function
__main__()

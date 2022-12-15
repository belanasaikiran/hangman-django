import random
words = ["hangman", "python", "audacix", "bottle", "pen"]

# The player should be allowed to guess incorrectly 1/2 the number of characters in the
# word. So for example if the selected word in "Pen", the player can make 2 incorrect
# guesses before loosing the game.


game_word = random.choice(words)
game_word_len = len(game_word)


def init():
    print("Welcome to Hangman! 🕴")
    # print(game_word)

# def fill():

#     while True:
#         option = input("Guess a letter: ")

#         if len(option) == 1:
#             print(option)
#             break
#         else:
#             print('Enter a single letter only')
#             continue


#     if option in game_word:
#         print(option, " exists")
#         findLetter = game_word.find(option)
#         print("found letter at index", findLetter)

#         Fill_Letters = Fill_Letters[:findLetter] + option + Fill_Letters[findLetter + 1:]
#         print(Fill_Letters)

#     else:
#         print(option, " doesn't exist in word")


def __main__():
    init()

    # print(game_word_len)
    print("Enter a word for", game_word_len, "letters")
    Fill_Letters = game_word_len * "_"
    print(Fill_Letters)
    print("\n")

    # The player should be allowed to guess incorrectly 1/2 the number of characters in the word.

    chances = game_word_len//2 #floor division
    print("You have", chances, " remaining chances")

    while True:

        if "_" in Fill_Letters:
            print("we need to fill the remaining spaces")

            for i in range(chances):
                print("You have", i, " remaining chances")
                while True:
                    option = input("Guess a letter: ")

                    if len(option) == 1:
                        # print(option)
                        break
                    else:
                        print('Enter a single letter only')
                        continue


                if option in game_word:
                    print(option, " exists")
                    findLetter = game_word.find(option)
                    # print("found letter at index", findLetter)

                    Fill_Letters = Fill_Letters[:findLetter] + option + Fill_Letters[findLetter + 1:]
                    print(Fill_Letters)

                else:
                    print(option, " doesn't exist in word")
            continue
        else:
            print("You Win!")
            break












# Execute main function
__main__()
from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse, JsonResponse

# import model game
from hangman.models import Game
import os


####### PYTHON ######
import random
words = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

guessedLetters = []



def get_word():
    game_word = random.choice(words).upper()
    return game_word


def get_chances(LatestGameWord, request):
    word = LatestGameWord

    if request.method == 'GET':
        game_word_len = len(word)
        chances = game_word_len//2  # floor division
        if (game_word_len < 5):
            chances = 3
            return chances
    else:
        chances = ""
        # chances = chances - 1
    return chances


def get_FillLetters(LatestGameWord, request, alphabet):
    Fill_Letters = len(LatestGameWord) * "_"
    if request.method == 'GET':
        fillLetters = Game(fill_Letters=Fill_Letters)
        fillLetters.save()
        LatestFillWord = Game.objects.last().fill_Letters
        print(LatestFillWord)
        return LatestFillWord
    else:
        if "_" in Fill_Letters:
            LatestFillWord = Game.objects.last().fill_Letters
            print("YAY")
        # return LatestFillWord

#  ##### DJANGO ####


def game(request):

    if request.method == 'GET':

        # Game Status
        status = "Game in progress"

        # clear guessLetters
        guessedLetters.clear()
        # get random word
        word = get_word()
        print("Word is", word)
        # save random word to DB
        gameWord = Game(game_word=word)
        gameWord.save()
        LatestGameWord = Game.objects.last().game_word
        chances = get_chances(LatestGameWord, request)
        # Fill Letters
        Fill_Letters = len(LatestGameWord) * "_"
        print(Fill_Letters)
        WordsAndChances = Game(
            game_word=word, chances=chances, fill_Letters=Fill_Letters)
        WordsAndChances.save()
        print("GameWord, FillLetters & Chances are:", WordsAndChances.game_word,
              WordsAndChances.fill_Letters,  WordsAndChances.chances)

        ChancesLeft = Game.objects.last().chances
        print("Chances Left:",  ChancesLeft)


        AllAlphabets = True

        ######

        # Generate empty blank spaces
        # alphabet = ""
        # # Fill_Letters = get_FillLetters(LatestGameWord, request, alphabet)
        # # print(Fill_Letters)
        # print("\nAvailable Letters: \n", alphabets)


        # for i in range(97, 123):
        #     print(chr(i).upper())
        #     renderButtons('Alphabets.html', i)


        return render(request, 'Hangman.html', {'chancesLeft': ChancesLeft, 'MissionWord': Fill_Letters, 'status': status, 'alphabet': 'A', 'AllAlphabets': AllAlphabets})

    # game_word = game_word
    # print(game_word)

    if request.method == 'POST':
        status = "Game in progress"
        alphabet = request.POST['letter']
        print("alphabet pressed:", alphabet)
        LatestGameWord = Game.objects.last().game_word
        ChancesLeft = Game.objects.last().chances
        # print("Chances Left:",  ChancesLeft)
        print("Chances Left:", ChancesLeft)
        GuessesList = ''
        RevealWord = ''


        #  add guess letters
        if alphabet in guessedLetters:
            print("Already Guessed")
            GuessesList =GuessesList
        else:
            guessedLetters.append(alphabet);
            print(guessedLetters)
            latestGuesses = len(guessedLetters)
            print("len", latestGuesses)
            guesses = Game.objects.update(guessedLetters=guessedLetters)
            print("From DB:", guesses)
            # guessedLetters = str(guessedLetters)[1:-1]
            print(str(guessedLetters)[1:-1])
            x=str(guessedLetters)
            x=x.replace("[","")
            x=x.replace("]","")
            x=x.replace("'","")
            GuessesList = x
            




        #  Filling Spaces
        LatestFillWord = Game.objects.last().fill_Letters
        print("Used Words", LatestFillWord)
  


        if alphabet in LatestGameWord:
            print(alphabet, " exists in word")
            #  check for remaining spaces
            if "_" in LatestFillWord:
                for i in range(len(LatestGameWord)):
                    if (alphabet == LatestGameWord[i]):
                        Fill_list = list(LatestFillWord)
                        Fill_list[i] = alphabet
                        LatestFillWord = ''.join(Fill_list)
                        # print(LatestFillWord)
                        Game.objects.update(fill_Letters=LatestFillWord)
                        status = "That's great!, Now try the remaining ones"
                        AllAlphabets = True

                Fill_Letters = get_FillLetters(LatestGameWord, request, alphabet)
        else:
            print("Wrong 😐, Try a different one \n")

            # ChancesLeft = ChancesLeft - 1
            ChancesLeft = Game.objects.last().chances

            # verify chances
            if ChancesLeft < 2:
                ChancesLeft = 0
                Game.objects.update(chances=ChancesLeft)
                print("Chances Left:",  ChancesLeft)
                status = 'You have Lost the Game,  Click *New Game* to play again'
                AllAlphabets = False
                RevealWord = LatestGameWord


            else:
                ChancesLeft = ChancesLeft - 1
                Game.objects.update(chances=ChancesLeft)
                print("Chances Left:",  ChancesLeft)
                status = "Wrong 😐 Try a different one"
                AllAlphabets = True
                RevealWord = ''




        if Game.objects.last().game_word == Game.objects.last().fill_Letters:    
            print(Game.objects.last().game_word, Game.objects.last().fill_Letters)
            status = "Congrats, You Win! 🥳 🎉"
            AllAlphabets = False
            RevealWord = LatestGameWord
            print(status)

        return render(request, 'Hangman.html', {'chancesLeft': ChancesLeft, 'MissionWord': LatestFillWord, 'status': status, 'GuessedLetters': GuessesList, 'AllAlphabets': AllAlphabets, 'RevealWord': RevealWord})


def index(request):
    # return HttpResponse("Hello, World!")

    return game(request)


#  When guessing for post requests
def guess(request):
    return game(request)




def renderButtons(alphabet, i):
    html = '''<button class='bg-cyan-800 p-2 2xl:w-24 2xl:h-24 w-16 h-16 hover:bg-yellow-400 hover:text-cyan-900 transition-all duration-500 rounded-sm hover:scale-125 hover:rounded-full' type='submit' name='letter' value={{alphabet}} id='btn1' > {{alphabet}} </button>'''
    print(html)
    print(alphabet)
    return alphabet, i


# NOTES:
# 1. To get last entry in specific row, we use
# ```
# Game.objects.last().game_word
# ```
# Example:
    # word = get_word()
    # print("Word is", word)
    # gameWord = Game(game_word=word)
    # gameWord.save()
    # LatestGameWord = Game.objects.last()
    # print("last Word is:", LatestGameWord.game_word )

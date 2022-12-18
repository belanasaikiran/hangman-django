from django.shortcuts import render
from django.template import RequestContext

# Create your views here.
from django.http import HttpResponse, JsonResponse

# import model game
from hangman.models import Game


####### PYTHON ######
import random
words = ["Hangman", "Python", "Audacix", "Bottle", "Pen"]

alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


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
        return LatestFillWord

#  ##### DJANGO ####
def game(request):

    if request.method == 'GET':
        # get random word
        word = get_word()
        print("Word is", word)
        # save random word to DB
        # gameWord = Game(game_word=word)
        # gameWord.save()
        noOfChances = Game(chances=chances)
        chances = get_chances(LatestGameWord, request)
        WordsAndChances = Game(game_word=word, chances=chances)
        WordsAndChances.save()
        LatestGameWord = Game.objects.last().game_word
        
        print(LatestGameWord)
        print("GameWord & last Word is:", WordsAndChances)

        # check for no. of chances
        # noOfChances.save()
        ChancesLeft = Game.objects.last().chances
        print("Chances Left:",  ChancesLeft)

        # Generate empty blank spaces
        alphabet = ""
        Fill_Letters = get_FillLetters(LatestGameWord, request, alphabet)
        # print(Fill_Letters)
        print("\nAvailable Letters: \n", alphabets)
        # render
        return render(request, 'Hangman.html', {'chancesLeft': ChancesLeft, 'MissionWord': Fill_Letters})

    # game_word = game_word
    # print(game_word)


    if request.method == 'POST':
        alphabet = request.POST['letter']
        print("alphabet pressed:", alphabet)
        LatestGameWord = Game.objects.last().game_word
        ChancesLeft = Game.objects.last().chances
        # print("Chances Left:",  ChancesLeft)
        print("Data from model:",ChancesLeft)

        if alphabet in LatestGameWord:
            print("The Letter exists in word")
            Fill_Letters = get_FillLetters(LatestGameWord, request, alphabet)
        else:
            print("Wrong 😐, Try a different one \n")
            # ChancesLeft = ChancesLeft - 1
            print("Chances Left:",  ChancesLeft)


        return render(request, 'Hangman.html', {'chancesLeft': ChancesLeft, 'MissionWord': 'word'})


def index(request):
    # return HttpResponse("Hello, World!")

    return game(request)


#  When guessing for post requests
def guess(request):
    return game(request)


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

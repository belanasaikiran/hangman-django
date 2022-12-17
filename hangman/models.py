from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    game_word = models.CharField(max_length=20)
    game_word_len = models.CharField(max_length=20, default="")
    status = models.CharField(max_length=10, default="In Progress")
    guessedLetters = models.CharField(max_length=20, default="")
    fill_Letters = models.CharField(max_length=20, default="")
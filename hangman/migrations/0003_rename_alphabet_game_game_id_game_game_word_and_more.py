# Generated by Django 4.1.4 on 2022-12-17 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0002_game_delete_book'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='alphabet',
            new_name='game_id',
        ),
        migrations.AddField(
            model_name='game',
            name='game_word',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='game',
            name='game_word_len',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='game',
            name='guessedLetters',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(default='In Progress', max_length=10),
        ),
    ]

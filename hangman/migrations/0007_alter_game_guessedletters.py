# Generated by Django 4.1.4 on 2022-12-18 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0006_game_chances'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='guessedLetters',
            field=models.CharField(default='', max_length=30),
        ),
    ]

from django.db import models


class Game(models.Model):
    players = models.ManyToManyField('players.Player')

    referee = models.ForeignKey(
        'players.Player',
        on_delete=models.CASCADE,
        null=True,
        related_name='game_name',
    )

    tournament_name = models.TextField(
        default='',
        max_length=50,
    )

    type = models.CharField(
        max_length=7,
        choices=(
            ('Singles', 'Singles'),
            ('Doubles', 'Doubles'),
        )
    )

    location = models.CharField(
        default='',
        max_length=20,
    )

    def __str__(self):
        return self.tournament_name

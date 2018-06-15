from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class PlayerManager(UserManager):
    pass


class Player(AbstractUser):

    objects = PlayerManager
    user = AbstractUser()

    active = models.BooleanField(
        default=True
    )

    is_referee = models.BooleanField(
        default=False
    )

    wins = models.IntegerField(
        default=0,
    )

    losses = models.IntegerField(
        default=0,
    )

    player_bio = models.TextField(
        blank=True,
        default='',
        max_length=280,
    )

    player_ranking = models.ForeignKey(
        'ranking.Ranking',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='player_ranking',
    )

    def __str__(self):
        return self.user.get_username()

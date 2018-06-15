from django.db import models


class Ranking(models.Model):
    tier = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('Recreational', 'Recreational'),
        )
    )

    number_of_players = models.IntegerField(
        default=0,
    )

    class Meta:
        verbose_name = 'Ranked Tier'

    def __str__(self):
        return self.tier

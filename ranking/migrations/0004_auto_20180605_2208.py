# Generated by Django 2.0.5 on 2018-06-05 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20180605_2208'),
        ('ranking', '0003_auto_20180605_2201'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ModelRanking',
            new_name='Ranking',
        ),
    ]

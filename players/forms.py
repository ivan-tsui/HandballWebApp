from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Player


class PlayerCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Player
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'player_bio',
        )


class PlayerChangeForm(UserChangeForm):

    class Meta:
        model = Player
        fields = UserChangeForm.Meta.fields

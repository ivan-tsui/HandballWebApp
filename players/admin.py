from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import PlayerCreationForm, PlayerChangeForm
from .models import Player


class PlayerAdmin(UserAdmin):
    model = Player
    add_form = PlayerCreationForm
    form = PlayerChangeForm


admin.site.register(Player, PlayerAdmin)

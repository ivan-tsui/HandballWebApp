from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views import generic
from .forms import PlayerCreationForm
from .models import Player


# def index(request):
#     player_list = Player.objects.order_by('user.username')
#     template = loader.get_template('players/index.html')
#     context = {
#         'player_list': player_list,
#     }
#     return HttpResponse(template.render(context, request))


class HomePageView(TemplateView):
    template_name = 'players/home.html'


class SignUp(generic.CreateView):
        form_class = PlayerCreationForm
        success_url = reverse_lazy('login')
        template_name = 'registration/signup.html'

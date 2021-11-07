from django.shortcuts import render
from django.views import generic
from .models import Game


class GameListView(ListView):
    """
    Class Based View listing the user information and game details.
    """
    model = Game
    template_name = 'core/index.html'
    context_object_name = 'games'
    ordering = ['-date-posted']
    paginate = 25


class GameCreateView(Createview):
    """
    Class Based View detailing how to create user information.
    """
    model = Game
    fields = ['name', 'viewer_hour', 'hours_streamed', 'acv_num', 'creators', 'streams_num']
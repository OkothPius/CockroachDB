from django.urls import path
from .views import GameListView, GameCreateView

urlpatterns = [
    path('', GameListView.as_view(), name='home'),
    path('new/', GameCreateView.as_view(), name='game-create'),
]

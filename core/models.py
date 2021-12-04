from django.db import models
from django.urls import reverse


class Game(models.Model):
    """
    This is a Game model class.
    """
    name = models.CharField(max_length=100)
    viewer_hour = models.PositiveIntegerField()
    hours_streamed = models.PositiveIntegerField()
    acv_num = models.PositiveIntegerField()
    creators = models.PositiveIntegerField()
    streams_num = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}'

    # Handles redirect
    def get_absolute_url(self):
        return reverse('home')

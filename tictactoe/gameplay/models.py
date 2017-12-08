from django.db import models
# import default user class
from django.contrib.auth.models import User


class Game(models.Model):
    first_player = models.ForeignKey(User,
                                     related_name='games_first_player', on_delete=models.CASCADE)
    second_player = models.ForeignKey(User,
                                      related_name='games_second_player', on_delete=models.CASCADE  )

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F')


class Move(models.Model):
    # (primary key field added by django)
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length=300, blank=True)

    # who made the move?
    by_first_player = models.BooleanField()

    # add relation from moves to games
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # with django_2 the on_delete argum ent signifies that if the game
    # gets deleted, so do the related attributes (like moves)

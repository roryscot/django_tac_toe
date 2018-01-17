from django.db import models
# import default user class
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse


GAME_STATUS_CHOICES = (
    ('F', 'First PLayer to Move'),
    ('S', 'Second Player to Move'),
    ('W', 'First Player Wins!'),
    ('L', 'Second Player Wins!'),
    ('D', 'Draw'),
)

class GamesQuerySet(models.QuerySet):
    def games_for_user(self, user):

        return self.filter(
            Q(first_player=user) | Q(second_player=user)
        )

    def active(self):
        return self.filter(
            Q(status='F') | Q(status= 'S')
        )

class Game(models.Model):
    first_player = models.ForeignKey(User,
                                     related_name='games_first_player', on_delete=models.CASCADE)
    second_player = models.ForeignKey(User,
                                      related_name='games_second_player', on_delete=models.CASCADE  )

    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='F')

    #overwrite objects attribute that normally references the default manager
    objects = GamesQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('gameplay_detail', args=[self.id])

    def __str__(self):
        return "{0} vs {1}".format(
            self.first_player, self.second_player
        )


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

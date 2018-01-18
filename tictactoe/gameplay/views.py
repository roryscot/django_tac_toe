from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Game
from .forms import MoveForm

@login_required()
def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)
    context = {'game': game}
    #the template will only get the form object on a user's turn
    if game.is_users_move(request.user):
        context['form'] = MoveForm()
    return render(request,
                  "gameplay/game_detail.html",
                  context)

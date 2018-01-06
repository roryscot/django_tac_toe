from django.shortcuts import render, redirect

def welcome(request):
    if request.user.is_authenticated:
        return redirect('player_home') #argument is a string so that it redirects to the name of the url
    return render(request, 'tictactoe/welcome.html')
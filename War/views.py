from django.shortcuts import get_object_or_404, redirect, render
from .models import Player
from .forms import PlayerForm
from .war_logic import *

# Create your views here.
def war_home(request):
    return render(request, 'War/war_home.html')

def players(request):
    players = Player.players.all()
    context = {'players': players}
    return render(request, 'War/players_list.html', context)

def add_player(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('players')
    else:
        print(form.errors)
        form = PlayerForm()
    return render(request, 'War/add_player.html', {'form': form})

def delete_player(request, id):
    id = int(id)
    player = get_object_or_404(Player, id=id)
    if request.method == 'POST':
        player.delete()
        return redirect('players')
    return render(request, 'War/delete_player.html', {'player': player})

def confirm_delete(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST or None)
        if form.is_valid():
            return redirect('players')
        else:
            return redirect('players')

def player1(request):
    players = Player.players.all()
    context = {'players': players}
    return render(request, 'War/player1.html', context)

def player2(request, id):
    players = Player.players.all()
    player1 = Player.players.get(id=id)
    context = {
        'players': players,
        'player1': player1,
        }
    return render(request, 'War/player2.html', context)

def play(request, id, id2):
    player1 = Player.players.get(id=id)
    player2 = Player.players.get(id=id2)
    game = WarGame()
    winner = None
    loser = None
    while winner == None:
        game.play_round()
        winner = game.check_for_win()
    if winner == 1:
        print("player1 wins the game")
        print("-------------------")
        winner = player1
        loser = player2
    if winner == 2:
        print("player2 wins the game")
        print("-------------------")
        winner = player2
        loser = player1
    winner.wins +=1
    winner.save()
    loser.losses +=1
    loser.save()

    context = {
        'player1': player1,
        'player2': player2,
        'winner': winner,
        'loser': loser,
        }

    return render(request, 'War/play.html', context)

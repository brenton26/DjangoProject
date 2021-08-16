from django.urls import path
from . import views

urlpatterns = [
    path('', views.war_home, name="war_home"),
    path('players/', views.players, name="players"),
    path('players/add/', views.add_player, name="add_player"),
    path('players/<int:id>', views.delete_player, name="delete_player"),
    path('play/', views.player1, name="player1"),
    path('play/<int:id>', views.player2, name="player2"),
    path('play/<int:id>/<int:id2>', views.play, name="play_war"),
]
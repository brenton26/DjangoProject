from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.CAH, name="CAH"),
    path('api/whitecards', views.WhiteCards.as_view(), name="white_cards"),
    path('api/whitecards/1', views.WhiteCards.as_view(), name="white_card"),
    path('api/blackcards', views.BlackCards.as_view(), name="black_cards"),
    path('api/blackcards/1', views.BlackCards.as_view(), name="black_card"),
]
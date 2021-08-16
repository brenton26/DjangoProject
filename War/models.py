from django.db import models
import random

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=30)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    players = models.Manager()

    def __str__(self):
        return self.name


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
    ranks = (
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
        ('6', 6),
        ('7', 7),
        ('8', 8),
        ('9', 9),
        ('10', 10),
        ('Jack', 11),
        ('Queen', 12),
        ('King', 13),
        ('Ace', 14)
    )    
    def __repr__(self):
        return(f"{self.rank[0]} of {self.suit}")


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Card.ranks for suit in Card.suits]

    def shuffle(self):
        shuffled_deck = random.shuffle(self.cards)
        return shuffled_deck

    def deal(self):
        player1_hand = self.cards[::2] 
        player2_hand = self.cards[1::2]
        return (player1_hand, player2_hand)

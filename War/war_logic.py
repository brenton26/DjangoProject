from .models import *


class WarGame():
    def __init__(self):
        deck = Deck()
        deck.shuffle()
        (self.player1_hand, self.player2_hand) = deck.deal()

    def play_round(self):
        print("---------------Player1 Hand------------------")
        print(self.player1_hand)
        print("---------------Player2 Hand------------------")
        print(self.player2_hand)
        print("---------------------------------------------")
        player1_card = self.player1_hand[0]
        player2_card = self.player2_hand[0]
        print(f"player 1 plays the {player1_card} | player 2 plays the {player2_card}")
        print("---------------------------------------------")
        if player1_card.rank[1] > player2_card.rank[1]:
            print("player 1 wins the round!")
            print("------------------------")
            losing_card = self.player2_hand.pop(0)
            winning_card = self.player1_hand.pop(0)
            self.player1_hand.extend([losing_card, winning_card])
        elif player1_card.rank[1] < player2_card.rank[1]:
            print("player 2 wins the round!")
            print("------------------------")
            losing_card = self.player1_hand.pop(0)
            winning_card = self.player2_hand.pop(0)
            self.player2_hand.extend([losing_card, winning_card])
        else:
            print("it's war!!!")
            print("--------------------")
            self.war()

    def war(self, previous_bounty=[]):
        if len(self.player1_hand) >=5 and len(self.player2_hand) >=5:
            print("*Both players lay their top 3 cards on the table*")
            player1_bounty = [self.player1_hand[:4]][0]
            self.player1_hand = self.player1_hand[4:]
            player2_bounty = [self.player2_hand[:4]][0]
            self.player2_hand = self.player2_hand[4:]
            print("-------player1bounty-------")
            print(player1_bounty)
            print("---------------------------")
            print("-------player2bounty-------")
            print(player2_bounty)
            print("---------------------------")
            bounty = player1_bounty + player2_bounty + previous_bounty
            print("-------total_bounty--------")
            print(bounty)
            print("---------------------------")
            player1_war_card = self.player1_hand[0]
            player2_war_card = self.player2_hand[0]
            print(f"player 1 plays the {player1_war_card} | player 2 plays the {player2_war_card}")
            if player1_war_card.rank[1] > player2_war_card.rank[1]:
                print("player 1 wins the war!")
                print("--------------------")
                losing_card = self.player2_hand.pop(0)
                winning_card = self.player1_hand.pop(0)
                self.player1_hand.extend([losing_card, winning_card])
                self.player1_hand += bounty
            elif player1_war_card.rank[1] < player2_war_card.rank[1]:
                print("player 2 wins the war!")
                print("----------------------")
                losing_card = self.player1_hand.pop(0)
                winning_card = self.player2_hand.pop(0)
                self.player2_hand.extend([losing_card, winning_card])
                self.player2_hand += bounty
            else:
                print("it's another war!!!")
                print("-------------------")
                self.war(previous_bounty=bounty)
        elif len(self.player1_hand) < 5:
            print("player1 has run out of cards!")
            print("------------------------------")
            self.player2_hand += self.player1_hand
            self.player1_hand = []
        elif len(self.player2_hand) < 5:
            print("player2 has run out of cards!")
            print("------------------------------")
            self.player1_hand += self.player2_hand
            self.player2_hand = []

    def check_for_win(self):
        if self.player1_hand == [] or self.player2_hand == []:
            print("------------------")
            print("Win condition met!")
            print("------------------")
        if self.player2_hand == []:
            return 1
        if self.player1_hand == []:
            return 2



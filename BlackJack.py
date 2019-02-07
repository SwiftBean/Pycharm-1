import random
class Card(object):
    """A playing card
    this class will build a single card.
    To build a card, call Card() and pass in a rank and a suit.
    card1 = Card(rank = "A", suit = "s")
    """
    ranks = ["A","2","3","4","5","6","7",
             "8","9","10","J","Q","K"]
    suits = ["c","d","h","s"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.face_up = True

    def __str__(self):
        rep = self.rank + self.suit
        return rep

    def flip(self):
        self.face_up = not self.face_up

class Hand(object):
    """This is the hand that you play with."""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []
    def add(self, card):
        self.cards.append(card)
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

import random
class Card(object):
    """A playing card
    this class will build a single card.
    To build a card, call Card() and pass in a rank and a suit.
    card1 = Card(rank = "A", suit = "s")
    """
    ranks = ["A","2","3","4","5","6","7",
             "8","9","10","J","Q","K"]
    suits = ["♣","♦","♥","♠"]

    def __init__(self,rank,suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.face_up = not self.face_up
#############################################################################################
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
#############################################################################################
class Deck(Hand):
    """This is your deck. It allows you to pass out cards to other players, and it
    is comprised of cards in suits of hearts, clubs, spades, and diamonds."""
    def populate(self):
        for suit in Card.suits:
            for rank in Card.ranks:
                self.add(Card(rank, suit))
    def shuffle(self):
        import random
        random.shuffle(self.cards)
    def deal(self, hands, per_hand= 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)

                else:
                    print("Can't continue to deal. Out of cards.")
#############################################################################################

#############################################################################################
if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")


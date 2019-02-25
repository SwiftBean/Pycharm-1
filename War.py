#Zachary Page, Isaac Arthur, Cody Dzierzon
#02/21/19
#War
#########################################################################################
# imports
import cards, games


#########################################################################################
# Classes
class War_Card(cards.Card):
    ace_value = 1

    @property
    def value(self):
        if self.is_face_up:
            v = War_Card.ranks.index(self.rank) + 1
        else:
            v = None
        return v
#########################################################################################
class War_Deck(cards.Deck):
    def populate(self):
        for suit in War_Card.suits:
            for rank in War_Card.ranks:
                self.cards.append(War_Card(rank, suit))
#########################################################################################
class War_Hand(cards.Hand):

    def __init__(self, name):
        super(War_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(War_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if a card in the hand has a value of None, then the total is None
        for card in self.cards:
            if not card.value:
                return None
        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
            t += card.value

    @property
    def is_busted(self):
        return self.total == 0
#########################################################################################
class War_Player(War_Hand):
    """This is the Solider."""

    def play(self, hand):
        top_card = self.cards[0]
        self.give(top_card, hand)

    def lose(self):
        print(self.name, "loses.")
        self.cards.clear()

    def win(self):
        print(self.name, "wins.")
#########################################################################################
class War_Pot(War_Hand):


    @property
    def check_winner(self):
        if self.cards[0].value > self.cards[1].value:
            winner = 0
        elif self.cards[0].value < self.cards[1].value:
            winner = 1
        else:
            winner = None
        return winner



    @property
    def check_winner_war(self):
        if self.cards[8].value > self.cards[9].value:
            winner = 0
        elif self.cards[8].value < self.cards[9].value:
            winner = 1
        else:
            winner = None
        return winner








#########################################################################################
class War_Game(object):
    def __init__(self, names):

        self.players = []
        for name in names:
            player = War_Player(name)
            self.players.append(player)

        self.pot = War_Pot("POT")

        self.deck = War_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def game_over(self):
        for player in self.players:
            x = len(player.cards)
            print(player.name, x)
            if x <= 0:
                return True
        return False

    def play(self):
        game_over = None
        self.deck.deal(self.players, per_hand=26)
        while not game_over:
            for player in self.players:
                player.play(self.pot)

            winner = self.pot.check_winner
            print(self.players[0].name + " ", self.pot, self.players[1].name)

            if winner == 0:
                print(self.players[0].name, "Wins")
            elif winner == 1:
                print(self.players[1].name, "Wins")


            else:
                p1len = len(self.players[0].cards)
                p2len = len(self.players[1].cards)
                if p1len >= 4 and p2len >= 4:
                    print("WAR")
                    for i in range(4):
                        for player in self.players:
                            player.play(self.pot)
                    print(self.pot)

                    winner = self.pot.check_winner_war
                    if winner == 0:
                        print(self.players[0].name, "Wins")

                    elif winner == 1:
                        print(self.players[1].name, "Wins")
                else:
                    if p1len <= 4:
                        self.players[0].lose()
                    else:
                        self.players[1].lose()









            self.pot.give_pot(winner)
            input("press enter to play")

            game_over = self.game_over()
#########################################################################################
# Main
def main():
    print("\t\tWelcome to War!\n")
    names = []
    number = 2
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    game = War_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again? (Y/N): ")

main()
input("\n\nPress the enter key to exit: ")
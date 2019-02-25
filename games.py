import cards


def display_puzzle():
    """"Displays a puzzle using string positions."""
    print(puzzle[0:10])
    print(puzzle[10:20])
    print(puzzle[20:30])
    print(puzzle[30:40])
    print(puzzle[40:50])
    print(puzzle[50:60])
    print(puzzle[60:70])
    print(puzzle[70:80])
    print(puzzle[80:90])
    print(puzzle[90:])
    print()

def pieces():
    """Get human and computer tokens to use later."""
    go_first = ask_permission("Do you want to go first? y or n?: ")
    if go_first == "y":
        print("\nYeah I think you need the headstart.")
        human = x
        computer = o
    else:
        print("\nOh, you think you're better than a computer?")
        computer = x
        human = o
    return computer, human

def human_move(board):
    """Get human move."""
    op = legal_moves(board)
    move = None
    while move not in op:
        move = ask_num("Where will you move? (0 - 8): ", 0, num_squares)
        if move not in op:
            print("\nThat's not a legal move you fool")
        else:
            print("Fine..")
            return move

def congrat_winner(the_winner, computer, human):
    """Congragulate the winner."""
    if the_winner != tie:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")
    if the_winner == computer:
        print("Ha, you got beat by a computer, you suck")
    elif the_winner == human:
        print("So you've beaten me... I hope you enjoyed it.")
    elif the_winner == tie:
        print("It seems that we have a tie... try harder next time.")

def move_player(self,player,board):
    """Moves the players across positions on a board using player tokens."""
    oldpos = player.position
    player.position = player.position + self.move
    if self.move>0:
        print("This space has a ladder, "+player.token+" moves up", self.move, "spaces.")
        input("Press enter to use the ladder.")
    if self.move<0:
        print("This space has a chute, "+player.token+" moves down",self.move,"spaces.")
        input("Press enter to go down the chute.")
    if self.move>0 or self.move<0:
        if player.player_num == 1:
            p1p[oldpos] = EMPTY
            p1p[player.position] = player.token
        elif player.player_num == 2:
            p2p[oldpos] = EMPTY
            p2p[player.position] = player.token
        elif player.player_num == 3:
            p3p[oldpos] = EMPTY
            p3p[player.position] = player.token
        elif player.player_num == 4:
            p4p[oldpos] = EMPTY
            p4p[player.position] = player.token
        board.displayboard()

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while True:
        try:
            response = int(input(question))
            if response in range(low, high):
                return response
            else:
                print("That's out of range.")
        except:
            print("That's not a number")

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

class Player(object):
    import cards
    """This is a player for a game."""
    def __init__(self, name):
        self.name = name
        self.hand = cards.Hand()
    def __str__(self):
        rep = self.name
        rep = rep+""+str(self.hand.cards[0])
        return rep

if __name__ == "__main__":
    print("You ran this module directly (and did not 'import' it).")
    input("\n\nPress the enter key to exit.")
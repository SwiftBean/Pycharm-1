class Player(object):
    def __init__(self):
        self.health = 100

    def shoot(self,enemy):
        print("You fire your blaster and hit the alien.")
        enemy.die()
    def get_hit(self):
        self.health -= 50

class Alien(object):
    """An alien in a shooter game."""
    def __init__(self):
        self.health = 100
    def die(self):
        print("The alien gasps and says,'Oh, this is it. This is the big one\n"\
              "Yes, it's getting dark now. Tell my 1.6 million larvae that I loved them...\n"\
              "Goodbye, cruel universe.")
    def get_hit(self):
        self.health -= 50
        if self.health <= 0:
            self.die()
player = Player()
alien = Alien()
while True:
    player.shoot(alien)
    input()

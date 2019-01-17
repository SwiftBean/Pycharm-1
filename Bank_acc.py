class Critter(object):
    total = 0

    def __init__(self,name):
        print("A critter has been born!")
        self.name = name
        Critter.total += 1

    def __str__(self):
        rep= "Critter object\n"
        rep += "name: " +self.name
        return rep

    @staticmethod
    def status():
        print("\nThe total number of critters is", Critter.total)



    def talk(self):
        print("Hi. I'm an instance of class Critter. My name is"+self.name)

crit = Critter("Bob")
crit2 = Critter("Frank")
crit3 = Critter("Joe")
obj = crit.__str__()
if obj == "Bob":
    print("Yes")
print(crit)
crit.talk()
print(crit2)
crit2.talk()
Critter.status()
print(crit.total)














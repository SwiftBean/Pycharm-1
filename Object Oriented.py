class Human(object):

    def __init__(self,name,hair_color,eye_color,height,weight,iq,gender,race):
        self.name =name
        self.hair_color=hair_color
        self.eye_color=eye_color
        self.height=height
        self.weight=weight
        self.iq=iq
        self.gender=gender
        self.race=race
    def intro_self(self):
        print("Hello, my name is" + self.name)
    def describe_self(self):
        print("I have" +self.hair_color+"hair")
        print("I have" +self.eye_color+"eyes")
        print("I am" ,self.height," ft. tall")
        print("I weigh",self.weight,"lbs")
        print("I am a "+self.race+""+self.gender+"with an iq of",self.iq)

    def learn(self):
        amy_iq = input("Amy, what is 2 + 2? :")

        if amy_iq == "4":
            amy.iq += 1
            print(amy.iq)
        else:
            print("Nope, that's not the correct answer")
    def bmi(self):
        print("Let's find what your bmi is based on your weight of", self.weight, "and your height of", self.height, "\n")
        num1 = self.weight*0.45
        num2 = self.height*0.025
        num3 = num2*num2
        bmi = num1/num3
        print("With these conversions, we can see if you are in the healthy range for your height.")
        if bmi >= 12 and bmi <=18:
            print("You are underweight")
        elif bmi >= 19 and bmi <=24:
            print("You are at a healthy weight")
        elif bmi >= 25 and bmi <=29:
            print("You are overweight")
        elif bmi >= 30 and bmi <= 42:
            print("You are obese")
        else:
            print("I was unable to calculate your bmi, this could be because it is too low or too high")


zach = Human("Zach","brown","hazel", 1000, 2490, 23,"na","white")

zach.intro_self()
bob = Human("Bob","yellow","black", 5.9 ,285, 60,"na","orange")

amy = Human("Amy","black","gray", 5.5, 125, 24,"na","red")

amy.intro_self()
bob.intro_self()
zach.intro_self()
zach.describe_self()
bob.describe_self()
amy.describe_self()
amy.learn()
zach.bmi()


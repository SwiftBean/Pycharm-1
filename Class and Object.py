class Identify(object):
    def __init__(self):
        self.name = input("Enter your name: ")
        self.address = input("Enter your address: ")
        self.phone_number = input("Enter your phone number: ")

    def show(self):
        print(self.name)
        print(self.address)
        print(self.phone_number)

identify = Identify()
identify.show()

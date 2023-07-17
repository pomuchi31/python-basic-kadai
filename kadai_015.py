class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
          
    def printinfo(self):
        print("Name:", self.name)
        print("Age:", self.age)

user = Human("太郎", 33)

user.printinfo()
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_name(self, name):
        self.name = name
    def show_name(self):
        print(self.name)

user = Human("太郎", 33)  
    
print(user.name)
print(user.age)
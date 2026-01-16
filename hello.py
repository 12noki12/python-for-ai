
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print("Bark!!!FuCK")
    def eat(self):
        return f"{self.name} is eating"

dog1 = Dog("dave")
dog1.name
dog1.bark()
dog2 = Dog("ruby")
dog1.eat()
print(dog1.bark)

print(dog1.eat())
print(dog2.eat())
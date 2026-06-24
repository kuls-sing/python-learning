class Animal:
    def __init__(self,  name):
        self.name = name
        
    def speaks(self):
        print(f"{self.name} makes sound")
        
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call Animal's __init__ to set self.name
        self.breed = breed       # add Dog's own extra attribute

    def speak(self):
        print(f"{self.name} says Woof!")

    def __str__(self):
        return f"Dog: {self.name} | Breed: {self.breed}"
        
class Cat(Animal):
    def speaks(self):
        print(f"{self.name} says Meow!")
        
d = Dog("Rex", "Labrador")
print(d)
d.speak()

c = Cat("Whiskers")
c.speaks()    # Whiskers says Meow!
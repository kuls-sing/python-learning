class Animal:
    def __init__(self,  name):
        self.name = name
        
    def speaks(self):
        print(f"{self.name} makes sound")
        
class Cat(Animal):
    def __init__(self, name, indoor= None):
        super().__init__(name)
        self.indoor = indoor
        
    def speaks(self):
        print(f"{self.name} says Meow!")
        
    def __str__(self):
        return f"Cat: {self.name} | Indoor: {self.indoor}"
 #       return super().__str__()
 
c = Cat("Whiskers", True)
print(c)
c.speaks()
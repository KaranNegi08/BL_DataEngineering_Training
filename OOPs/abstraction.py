from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say(self):
        return 20
    
    def move(self):
        return "Moving"

class English(Greet):
    def say(self):
        
        print("Hello")

a= English()
a.say()
print(a.move())
print(a.__class__.__mro__)
g= Greet()
print(g.move())

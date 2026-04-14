class Customer:
    def __init__(self, name, age):
        self.name= name
        self.age= age
    
    def intro(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")

c1= Customer("Karan Negi", 20)
c2= Customer("Kartik", 22)
c3=Customer("Divyansh", 21)

L= (c1, c2, c3)

for i in L:
    i.intro()
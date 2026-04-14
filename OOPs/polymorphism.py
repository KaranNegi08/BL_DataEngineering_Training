class Phone:
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price= price
        self.brand= brand
        self.camera= camera
    
    def buy(self):
        print("Buying a smartPhone")

class SmartPhone(Phone):
    # Method Overriding
    def buy(self):
        print("Buying a smartPhone ")
        super().buy() # calling parent class method

s=SmartPhone(10000, "Samsung", "48MP")
s.buy() 
        
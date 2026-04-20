class Product:
    def __init__(self,name,price):
        self.name=name
        self.price = price
        

class Cart:

    def __init__(self):
        self.items={}

    def add_product(self, product):
        if product.name in self.items:
            self.items[product.name] +=product.price
            print(f"One more {product.name} added to cart.")
        else:
            self.items[product.name] =product.price
            print(f"{product.name} added to cart.")

    
    def remove_product(self, product):
        if product.name in self.items:
            del self.items[product.name]
            print(f"{product.name} removed from cart.")
        else:
            print(f"{product.name} is not in the cart.")

    def total_price(self):
        # total=0
        # for v in self.items.values():
        #     total += v
        total = sum(self.items.values())
        print(f"Total price of items in cart: {total}")
        return total

    
    def total_items(self):
        print( {k: v for k, v in self.items.items()} )

    def discount(self, amount):
        discount_price= self.total_price() * (amount/100)
        final_amount= self.total_price() - discount_price
        print(f"Final amount to pay: {final_amount}")

p1 = Product("Mac Book", 85000)
p2= Product("iPhone", 120000)
p3= Product("iPad",160000)

cart= Cart()

cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)
cart.total_price()
# cart.remove_product(p1)
# cart.total_price()
cart.total_items()
cart.discount(10)
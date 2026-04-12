class Customer:

    def __init__(self, name, gender):
        self.name=name 
        self.gender=gender

def greet(customer):
    print(id(customer))
    if customer.gender == "Male":
        print(f"Hello Mr. {customer.name} sir.")
    else:
        print(f"Hello Ms. {customer.name} ma'am.")

cust= Customer("Karan Negi", "Male")
print(id(cust))
greet(cust)


class Customer:
    def __init__(self, name, gender, address):
        self.name= name
        self.gender=gender
        self.address= address

    def edit_profile(self, new_name, new_city, new_pincode, new_state):
        self.name= new_name
        self.address.change_address(new_city, new_pincode, new_state)
        
class Address:
    def __init__(self, city, pincode, state):
        self.city= city
        self.pincode= pincode
        self.state= state
    
    def change_address(self, new_city, new_pincode, new_state):
        self.city= new_city
        self.pincode= new_pincode
        self.state= new_state


add = Address("Agra", 282007, "Uttar Pradesh")
cust=Customer("karan", "Male", add)

# print(cust.name)
# print(cust.gender)
# print(cust.address.city)
# print(cust.address.pincode)
# print(cust.address.state)

cust.edit_profile("Kunnu", "Pune", 111001, "Maharashtra")
print(cust.address.city)
print(cust.address.pincode)
print(cust.address.state)
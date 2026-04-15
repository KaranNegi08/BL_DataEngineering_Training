class Atm:  

    __counter=0
    def __init__(self):
        # print(id(self))
        self.pin= ""
        self.balance=0
        self.sno=Atm.__counter
        Atm.__counter += 1
        self.menu()
    
    @staticmethod
    def get_counter():
        return Atm.__counter
    @staticmethod
    def set_counter(value):
        if type(value) == int:
            Atm.__counter = value
        else:
            print("Invalid value for counter. It must be an integer.")
    
       

    def menu(self):
        while True:

            user_input= input("""
        Hello, how would you like to proceed?
        1.Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit 
    """)
        
            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.deposit()
            elif user_input == "3":
                self.withdraw()
            elif user_input == "4":
                self.check_balance()
            elif user_input == "5":
                print("Exit")
                break
            else: 
                print("Bye")
        
    def create_pin(self):
        self.pin= input("Enter your pin: ")
        print("Pin set successfully")
    
    def deposit(self):
        temp= input("Enter your pin: ")
        if temp == self.pin:
            amount= int(input("Enter amount to deposit: "))
            self.balance += amount
            print(f"You have successfully deposited {amount} in you account")
        else:
            print("Invalid pin!!")
    
    def withdraw(self):
        temp= input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter amount to withdraw: "))

            if amount <= self.balance:
                self.balance -= amount
                print(f"You have successfully withdrawn {amount} from your account")
            else:
                print("Insufficient balance!!")
        else:
            print("Invalid pin!!")
    
    def check_balance(self):
        temp= input("Enter your pin: ")
        if temp == self.pin:
            print(f"Your balance is {self.balance}")
        else:
            print("Invalid pin!!")

a= Atm()
b=Atm()
c=Atm()

print(a.sno)
print(b.sno)
print(c.sno)
# a.check_balance()
    
class Bank:
        def __init__(self, name, balance=0):
            self.accounts={}
            self.name=name
            self.__balance=balance

        def create_account(self):
            account_number= input("Enter account number: ")
            if account_number in self.accounts:
                print("Account already exists.")
            else:
                self.accounts[account_number]=1
                print("Account created successfully.")
            
            deposit_amount= float(input("Enter initial deposit amount: "))
            self.deposit(account_number, deposit_amount)
        
        def deposit(self, account_number, amount):
            if account_number in self.accounts:
                self.__balance+=amount
                print(f"Deposited {amount} to account {account_number}. Current balance: {self.__balance}")
            else:
                print("Account does not exist.")

            self.check_balance(account_number)

        def withdraw(self, account_number, amount):
            if account_number in self.accounts:
                if self.__balance >= amount:
                    self.__balance -=amount
                    print(f"Withdrew {amount} from account {account_number}. Current balance: {self.__balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Account does not exists.")

        def check_balance(self, account_number):
            if account_number in self.accounts:
                print(f"Current balance is {self.__balance}")
            else:
                print("Account does not exist.")

        
a1 = Bank("SBI")
a1.create_account()

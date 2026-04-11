bool=True
while bool:
    num= int(input("Enter a Number:"))

    if(num>=1 and num <= 10):
        print(f"You entered {num}")
        bool=False
    else:
        print("Please enter a number between 1 and 10")


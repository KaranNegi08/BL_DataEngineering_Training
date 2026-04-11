name = input("Enter your name: ")

if len(name) < 3:
    print("Name should be at least 3 characters long.")
else:
    print(f"Hello {name}, How are you?")
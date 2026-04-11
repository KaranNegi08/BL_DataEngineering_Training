str= input("Enter a string: ")

for i in str:
    if str.count(i) == 1:
        print(f"First unique element is {i}")
        break
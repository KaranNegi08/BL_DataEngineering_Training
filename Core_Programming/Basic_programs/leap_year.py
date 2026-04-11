year= int(input("Enter a year: "))

if len(str(year)) != 4:
    print("Please enter a valid 4-digit year.")
    exit()

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
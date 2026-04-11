num = int(input("Enter a number: "))
is_prime= True

if num >0:
    for i in range(2, num):
        if num % i == 0:
            is_prime=False
            break
else:
    print("Please enter a positive number")
    exit()

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
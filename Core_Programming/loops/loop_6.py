num= int(input("Enter a number: "))
result=1
i=2
while(i<=num):
    result *= i
    i += 1
print(f"Factorial of {num} is {result}")

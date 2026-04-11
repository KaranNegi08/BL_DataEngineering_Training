numbers= [1,-2,-3,-4,5,6,-7,-8,9,10]
count=0
for num in numbers:
    if num > 0:
        print(num, end=", ")
        count += 1
print(f"\nThere are {count} positive numbers in the list.")
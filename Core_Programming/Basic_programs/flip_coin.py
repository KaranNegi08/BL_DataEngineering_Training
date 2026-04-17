import random

num_of_flips= int(input("Enter the number of times you want to flip the coin: "))

if num_of_flips <= 0:
    print("Number of flips should be a positive integer.")
    exit()

heads_count = 0
tails_count = 0

for i in range(num_of_flips):
    flip_result = random.random()
    if flip_result < 0.5:
        tails_count += 1
    else:
        heads_count += 1

print(f"Number of Heads: {heads_count}")
print(f"Number of Tails: {tails_count}")


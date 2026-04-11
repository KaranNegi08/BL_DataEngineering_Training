str= input("Enter a string: ")

reverse_str=""

for i in range(len(str), 0, -1):
    reverse_str += str[i-1]

print(reverse_str)
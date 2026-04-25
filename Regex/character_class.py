# find digits in given data
import re

# pattern = r'[a-z]'
# pattern = r'[^0-9]'
# pattern = r'[aeiou]'
# pattern = r'\d'
# data = "The price is $10259"
# match= re.finditer(pattern,data)

# for i  in match:
#     print(i.group())
#     # print(i.start())

# match2= re.findall(pattern,data)
# print(match2)



#condition for password: 1. contains at least one digit or at least one uppercase letter
password= input("Enter password: ")
pattern = r'[0-9A-Z]'
match  = re.findall(pattern,password)

if match:
    print("Password Valid ")
else:
    print("Password is not valid.")
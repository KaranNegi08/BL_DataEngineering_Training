import re

data= " 1 90987688 53 416"
# pattern = r'\d{4}'
# pattern = r'\d{2,5}'   #between 2 to 5 digits
# pattern = r'\d{3,}'   #Minimum 3 digits
pattern = r'\d{,4}'  #Maximum 4 digits
match= re.findall(pattern,data)
print(match)

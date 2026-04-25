import re

# regular expression objects: - re.compile(pattern,flags)
# pattern=re.compile(r"thE", re.IGNORECASE)
# data= "the language python is very ppular python "

# match = re.search(pattern,data)
# match2 = re.match(pattern,data) #SEARCH AT THE BEGINNING
# print(match)

# if match2:
#     print(f"{match2} \n {match2.group()}")
    
# else:
#     print("Not found")



pattern = re.compile('ab', re.IGNORECASE)
data= 'abaababa'

# match = re.finditer(pattern,data)
# print(type(match))

# for i in match:
#     print(f"Start: {i.start()}, End: {i.end()}, Element: {i.group()}")
    

match2 = re.findall(pattern,data)
print(type(match2))
print(match2[0])
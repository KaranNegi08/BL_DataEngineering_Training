import re

data= "Email address: kk@gmail.com, jay@gmail.com, dishant@gmail.com"
pattern = r'(\w+)@(\w+)(\.\w+)'
match= re.findall(pattern,data)
for m in match:
    print("username: ", match[0])
    print("domain name: ", match[1])
    print("website type: ", match[2])
    print("="*50)
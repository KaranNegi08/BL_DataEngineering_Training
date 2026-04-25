import re
# data = "i am Data Enneeeenegineer"
# pattern = r'(ne)+'


# data= 'marks are 90,45,5521'
# pattern = r'\d+'

# data= "My email address are karan@gmail.com and karannegi.agra@gmail.com"
# pattern = r'[a-zA-Z0-9._]+@[a-zA-Z0-9.]+[a-zA-Z]' 

# data= "abb ac aaabbb aaa aaabbcc cc bb"
# pattern = r'a*b+\w+'

# data= """0hello world451
# welcome to my place 999"""
# pattern = r'\d{3}$'

# match= re.findall(pattern,data, re.MULTILINE)

# print(match) 

# data= "colour and color are same"
# pattern = r'colou?r'
# data= "Call me at 123-456-7890 or 9874561237"
# pattern = r'\d{3}[-]?\d{3}[-]?\d{4}?'

# match = re.findall(pattern,data)
# print(match)

# pattern = r'https?://\w+\.\w+'
# urls = ["http://example.com1", "https://example.org", "htttp://fileserver.net"]
# for url in urls:
#     if re.match(pattern,url):
#         print(f"Valid url: {url}")

# | pipe symbol

# pattern= r'dog|cat'
# text= "I have a dog or cat"

# matches= re.findall(pattern,text)
# print(matches)

pattern= r'\d{10}|[\w\.-]+@\w+\.\w+\b'
data= "kk: - 1234567899\n kkemail:- kk.agra@gmail.com"
match= re.findall(pattern, data)
print(match)
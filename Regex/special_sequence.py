import re

# text= "Hello,..  my phoneno.__[]  ]  [] is 123-456-7892"
text= "Today is 2023-10-02, and I have a meeting scheduled for 2023-10-05"


# pattern= r'\D'
# pattern =r'\w'
# pattern = r'\s'
# pattern= r'\S'
# pattern= r'\b'
# pattern = r'\bphone\b'
# pattern = r'\AHello'
# pattern = r'\.'
# pattern = r'\[\]'
pattern = r'\d{4}-\d{2}-\d{2}'
result= re.findall(pattern, text)
print(result)
import json
l = [1,2,3,4]

# with open("demo.json", "w") as f:
#     json.dump(l,f)


d={
    "name":"aditya",
    "age":23,
    "gender":"male"
}


# with open("demo.json", "w") as f:
#     json.dump(d,f, indent=4)



# with open("demo.json" , "r") as f:
#     d = json.load(f)
#     print(d)
#     print(type(d))
    
 
t=(1,2,3,4,5,6)

with open("demo.json", "w") as f:
    json.dump(t,f)


# with open("demo.json", "r") as f:
#     print(type(json.load(f)))

class Person:
    def __init__(self,name, age):
        self.name=name
        self.age= age
    
    def display(self):
        print(f"Hi my name is {self.name} and my age is {self.age}. ")

p=Person("aditya", 23)

import pickle 
with open("person.pkl", "wb") as f:
    pickle.dump(p,f)

with open("person.pkl", "rb") as f:
    p= pickle.load(f)
    p.display()


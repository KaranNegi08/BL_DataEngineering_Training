import json
class Person:
    def __init__(self,name, phone,email,city):
        self.name= name
        self.phone=phone
        self.email=email
        self.city= city

    def to_dict(self):
        return {
            "name":self.name,
            "phone":self.phone,
            "email":self.email,
            "city":self.city
        }
        

class AddressBook:
    def __init__(self):
        self.persons={}

    def add_person(self,person):
        if person.name in self.persons:
            print("Person already exists!!")
        else:
            self.persons[person.name]= person
            print("Person added successfully..")

    def delete_person(self, name):
        if name in self.persons:
            del self.persons[name]
            print("Person deleted successfully..")
        else:
            print("Person not found!!")

    def search_person(self,name, email=None, phone=None):
        results=[]
        for person in self.persons.values():
            if person.name.lower() == name.lower() or person.email.lower() == email.lower() or person.phone == phone:
                results.append(person)

        return results
    
    def edit_person(self,name, phone=None, email=None,city=None):
        if name in self.persons:
            person= self.persons[name]
            if phone:
                person.phone= phone
            if email:
                person.email= email
            if city:
                person.city=city
            
            print("Personal details updated successfully..")
        else:
            print("Person not found!!")

    def save_json(self):
        data=[]

        for person in self.persons.values():
            data.append(person.to_dict())

        with open("address.json", "w") as f:
            json.dump(data,f, indent=4)
        
        print("Address saved...")

    def load_json(self):
        try:
            with open("address.json", "r") as f:
                data= json.load(f)

            for item in data:
                person= Person(**item)
                self.persons[person.name]= person
            print("Adress loaded successfully..")

        except FileNotFoundError:
            print("File not found!!")
        
        except json.JSONDecodeError:
            print("Invalid JSON file")


book =AddressBook()

p1= Person("Karan", "6397473369", "karannegi.agra@gmail.com", "Agra")
p2= Person("Dishant", "8997473369", "dishant@gmail.com", "Delhi")
p3= Person("Dev", "7777473369", "dev@gmail.com", "UK")



book.load_json()
book.add_person(p2)
book.save_json()  
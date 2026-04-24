import json

class Student:
    def __init__(self,name, marks):
        self.name= name
        self.marks= marks

    def display(self):
        print(f"Name: {self.name} , Marks: {self.marks} ")

    def to_dict(self):
        return {
            "name": self.name,
            "marks": self.marks
        }   
    

class StudentManager:
    def __init__(self):
        self.students= []

    # Add Students
    def add_student(self,student):
        self.students.append(student)

    def display_student(self):
        if not self.students:
            print("No students found..")
        for s in self.students:
            s.display()

    def save_to_file(self, filename="students.json"):
        data= [s.to_dict() for s in self.students]
        with open(filename, "w") as f:
            json.dump(data,  f, indent=4)
        print("Data saved successfully....")

    def load_from_file(self, filename="students.json"):
        try:
            with open(filename, "r") as f:
                data= json.load(f)
            
            self.students=[]
            for item in data:
                student= Student(**item)
                self.students.append(student)
            print("Students loaded successfully...")
                    
        except FileNotFoundError:
            print("File not found!!!")
        except json.JSONDecodeError:
            print("Invalid JSON file")


if __name__ == "__main__":
    manager = StudentManager()
    manager.add_student(Student("Karan", 99))
    manager.add_student(Student("Dishant", 90))
    manager.add_student(Student("Rahul", 80))

    manager.save_to_file()

    manager.students={}
    manager.load_from_file()
    manager.display_student()



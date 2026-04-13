class User:
    def __init__(self):
        print("I am parent constructor")

    def login(self):
        print("User logged in")
    
    def register(self):
        print("User registered")

class Student(User):
    def __init__(self):
        super().__init__()
        print("I am child constructor")
    def enroll(self):
        print("Student enrolled")
    
    def review(self):
        print("Student reviewed the course")

s1=Student()

# s1= Student()
# s1.login()
# s1.register()
# s1.enroll()
# s1.review()
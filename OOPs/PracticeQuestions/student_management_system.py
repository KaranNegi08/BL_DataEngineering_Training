class Management:
    def __init__(self, name, roll_no, marks):
        self.students={}
        print(type(self.students))
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    
    def average_marks(self):
        return sum(self.marks)/len(self.marks)

    def grade(self):
        avg= self.average_marks()
        if avg >= 90:
            return "A"
        elif avg >=70:
            return "B"
        else:
            return "C"

s1= Management("Karan",72,[90,95,92,96])
print(s1.average_marks())
print(s1.grade())   
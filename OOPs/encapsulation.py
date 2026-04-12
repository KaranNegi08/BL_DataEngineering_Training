class A:
    def __init__(self):
        self.__x=10

    def get_x(self):
        return self.__x
    def set_x(self, new_x):
        if type(new_x) == int:
            self.__x=new_x
            print("Value of x is updated to:", self.__x)
        else:
            print("Invalid input. Please provide an integer value for x.")

a=A()
# print(a.get_x())
a.set_x(20)
print(a.__dict__)
#print(a._A__x)   #Name_Mangling
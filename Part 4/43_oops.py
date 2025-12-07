class Student:
    course = "python"
    def __init__(self,name):
        self.name = name
    
    def details(self):
        print(f"{self.name} hello")
        
obj1 = Student("Vijay")
obj1.details()
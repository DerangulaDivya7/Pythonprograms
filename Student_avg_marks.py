class Student:
    def __init__(self, marks): 
        self.marks = marks       

    def average(self):
       print( sum(self.marks) / len(self.marks))
marks_list = [85, 90, 78, 92, 88]
student = Student(marks_list)
student.average()

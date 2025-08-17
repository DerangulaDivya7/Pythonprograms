class person:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def getvalue(self):
        print("the  name is",self.name,"and rollno is",rollno)
name=(input())
rollno=int(input())
p=person(name,rollno)
p.getvalue()

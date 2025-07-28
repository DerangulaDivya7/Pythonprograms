class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sLL():
    def __init__(self):
     self.head=None
    def insert_begin(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=ne
    def display(self):
        if self.head is None:
            print("single linked list is empty")
        else:
           temp= self.head
           while temp:
               print(temp.data,"-->",end="")
               temp=temp.next
l=sLL()
n=Node(10)
l.head=n
n1=Node(20)
n.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
l.insert_begin(90)
l.insert_end(60)
l.insert_end(100)
l.display()

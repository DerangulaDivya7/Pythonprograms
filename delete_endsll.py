class Node:
    def __init__(self,data):
      self.data=data
      self.next=None
class sll:
   def __init__(self):
      self.head=None
   def display(self):
      if self.head is None:
         print("empty")
      else:
         temp=self.head
         while temp:
            print(temp.data,"--->",end=" ")
            temp=temp.next
   def del_end(self):
      prev=self.head
      temp=self.head.next
      while temp.next is not None:
         temp=temp.next
         prev=prev.next
      prev.next=None
l=sll()
n1=Node(10)
l.head=n1
n2=Node(20)
n1.next=n2
n3=Node(30)
n2.next=n3
n4=Node(40)
n3.next=n4
l.del_end()
l.display()

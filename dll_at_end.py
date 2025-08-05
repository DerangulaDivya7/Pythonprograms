class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("Doubly Linked List is empty")
        else:
            temp = self.head
            while temp:
                print(temp.data, "<-->", end=" ")
                temp = temp.next
            print("None")

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp


dll = DLL()
dll.insert_beginning(10)
dll.insert_beginning(15)
dll.insert_beginning(20)
dll.insert_beginning(5)
dll.insert_end(90)
dll.display()

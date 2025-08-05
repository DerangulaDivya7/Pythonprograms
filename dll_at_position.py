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
    def insert_position(self, pos, data):
        new_node = Node(data)
        if pos == 1:
            self.insert_beginning(data)
            return

        temp = self.head
        count = 1
        while temp is not None and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None or temp.next is None:
            self.insert_end(data)
        else:
            new_node.next = temp.next
            new_node.prev = temp
            temp.next.prev = new_node
            temp.next = new_node



dll = DLL()
dll.insert_beginning(10)
dll.insert_beginning(15)
dll.insert_beginning(20)
dll.insert_beginning(5)
dll.insert_end(90)
dll.insert_position(3,60)
dll.display()

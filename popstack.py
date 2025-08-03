class Stack(object):
    def __init__(self):
        self.stack=[]
        self.no_of_items=0
    def isEmpty(self):
        return self.stack==[]
    def push(self,data):
        self.stack.insert(self.no_of_items,data)
        self.no_of_items+=1
        return '{}'.format(data)
    def pop(self):
        self.no_of_items-=1
        data=self.stack.pop(self.no_of_items)
        return '{} Pop from stack'.format(data)
if __name__=='__main__':
    s=Stack()
    print(s.push(2))
    print(s.push(3))
    print(s.push(5))
    print(s.push(4))
    print(s.push(8))
    print(s.pop())
    print(s.pop())

class Queue(object):
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.insert(0,data)
        return '{}added into the queue'.format(data)
    def dequeue(self):
        return self.queue.pop()
    def sizeof(self):
        return '{}size of the queue'.format(len(self.queue))
if __name__=='__main__':
    q=Queue()
    print(q.enqueue(1))
    print(q.enqueue(7))
    print(q.enqueue(2))
    print(q.enqueue(4))
    print(q.enqueue(6))
    print(q.dequeue())
    print(q.dequeue())
    print(q.sizeof())

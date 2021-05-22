import queue
class Stack:
    def __init__(self):
        self.data = []

    # for inserting element
    q = queue.LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    q.put(4)
    while not q.empty():
        print(q.get())


    def pop(self):
        if self.isEmpty():
            print("Hey! Stack is Empty")
            return
        return self.data.pop()

    def top(self):
        if self.isEmpty():
            print("Hey! Stack is Empty")
            return
        return self.data[len(self.data)-1]
    def size(self):
        return len(self.data)

    def isEmpty(self):
         return self.size() == 0

s = Stack()
print("The size is:",s.size())
while s.isEmpty() is False:
     print(s.pop())
s.top()

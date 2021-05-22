class Stack:
    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

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
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print("The size is:",s.size())
while s.isEmpty() is False:
     print(s.pop())
s.top()

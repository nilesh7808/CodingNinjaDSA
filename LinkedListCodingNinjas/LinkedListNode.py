class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


a = Node(1)
b = Node(2)
a.next = b
print(a.data)
print(b.data)
print(a.next.data)
print(a)
print(a.next)
print(b)
print(b.next.data)

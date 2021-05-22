class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueUsingLL:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0

    def enqueue(self, data):
        newNode = Node(data)
        if self.__head is None:
            self.__head = newNode
        else:
            self.__tail.next = newNode
        self.__tail = newNode
        self.__count += 1

    def dequeue(self):
        if self.__head is None:
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data

    def front(self):
        if self.__head is None:
            return
        data = self.__head.data
        return data
    def isEmpty(self):
        return self.getSize() == 0

    def getSize(self):
        return self.__count

q = QueueUsingLL()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
while q.isEmpty() is False:
    print(q.dequeue(),"->",end=" ")
q.front()
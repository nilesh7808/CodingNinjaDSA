class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def search(head, value):
    count = 0
    curr = head
    while curr and curr.data != value:
        count += 1
        curr = curr.next
        if curr is None:
            return -1
    return count

def takeInput():
    inputll = list(int(i) for i in input().strip().split())
    head = None
    tail = None
    for currdata in inputll:
        if currdata == -1:
            break
        newNode = Node(currdata)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head


head = takeInput()
data = int(input())
print(search(head, data))
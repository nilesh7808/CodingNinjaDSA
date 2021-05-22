class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseLL(head):
    if head is None or head.next is None:
        return head

    t1 = head
    t2 = head.next

    while t2 is not None:
        t1.data, t2.data = t2.data, t1.data
    t1 = t1.next.next
    t2 = t2.next.next
    return head

def printll(head):
    while head is not None:
        print(str(head.data) +"->",end=' ')
        head = head.next
    print("None")
    print()

def takeInput():
    inputLL = [int (i) for i in input().strip().split()]
    head = None
    tail = None
    for currData in inputLL:
        if currData == -1:
            break
        newNode = Node(currData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

head =takeInput()
reverseLL(head)
printll(head)
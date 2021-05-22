class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data)+"-> ",end="")
        head = head.next
    print("None")
    return
def removeDuplicate(head):
    count = 0
    curr = head
    while head is not None:

def takeInput():
    inputLL = list(int (i) for i in input().strip().split())
    head = None
    tail = None
    for currdata in inputLL:
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
printLL(head)
removeDuplicate(head)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data) +"->",end="")
        head = head.next
    print(" None")
    return
def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count
def insert_at_Ith_Pos(head,i,data):
    if i < 0 or i >= length(head):
        return head
    count = 0
    prev = None
    curr = head
    while count < i:
        prev = curr
        curr = curr.next
        count = count + 1
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
    newNode.next = curr
    return head
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
i = int(input())
data = int(input())
printLL(head)
head = insert_at_Ith_Pos(head,i,data)
printLL(head)

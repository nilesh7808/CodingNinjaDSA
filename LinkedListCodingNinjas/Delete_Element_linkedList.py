class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printll(head):
    while head is not None:
        print(str(head.data) + "->",end="")
        head = head.next
    print("None")
    return
def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count
def delete(head,i):
    if i < 0 or i >= length(head):
        return head
    count = 0
    curr = head
    prev = None
    while count < i:
        prev = curr
        curr = curr.next
        count += 1
    if prev is not None:
        prev.next = curr.next
    else:
        head = curr.next
    return head
    pass
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
printll(head)
i = int(input())
head = delete(head,i)
printll(head)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data)+ "->",end="")
        head = head.next
    print("None")
    return
def insert_at_ith_recursive(head,i,data):
    if i < 0 :
        return head
    if i == 0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    if head is None:
        return None
    smallhead = insert_at_ith_recursive(head.next,i-1,data)
    head.next = smallhead
    return

def takeInput()  :
    inputLL = [int(i) for i in input().strip().split()]
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
head = insert_at_ith_recursive(head,i,data)
printLL(head)
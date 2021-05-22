class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def printLL(head):
    while head is not None:
        print(str(head.data) + "->",end=" ")
        head = head.next
    print(None)
    return
def takeInput():
    inputLL = [int (i) for i in input().strip().split()]
    head = None
    for j in inputLL:
        if j == -1:
            break
        newNode = Node(j)
        if head is None:
            head = newNode
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = newNode
    return head

head = takeInput()
printLL(head)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrange_LinkedList(head):
    if head is None:
        return

    oddH = None
    oddT = None
    evenH = None
    evenT= None
    while head is not None:
        if oddH == None:
            return
        if evenH == None:
            return
        if head.data % 2 != 0:
            oddH = head
            oddT = head
        head = head.next
        if head.data == 0:
            evenH = head
            evenT = head
        head = head.next
        oddT = oddT.next
        evenT = evenT.next
    oddT.next = evenT
    evenT.next = None
    return oddH

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()
arr=list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)

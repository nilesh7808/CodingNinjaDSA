class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def eliminate_duplicate(head):
    if head is None:
        return None
    t1 = head
    t2 = head.next
    if t2 is None:
        return head
    while t2 is not None:
        if t1.data == t2.data:
            t2 = t2.next
        else:
            t1.next = t2
            t1 = t2
            t2 = t2.next
    t1.next = t2
    return head
    pass

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
l = eliminate_duplicate(l)
printll(l)

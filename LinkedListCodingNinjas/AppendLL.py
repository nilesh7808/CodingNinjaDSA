class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append_LinkedList(head,n) :
    curr = head
    count = len(arr) - n - 1
    while count != 1:
        curr = curr.next
        count -= 1
    head2 = curr.next
    curr.next = None
    tail = head2
    while tail.next.next is not None:
        tail = tail.next
    tail.next.next = head
    return head2
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
i=int(input())
l = append_LinkedList(l, i)
printll(l)

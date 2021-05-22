class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def merge(head1,head2):
    
def mergeSort(head1):
    curr = head1
    tail = head1
    while curr.next != None and tail.next.next != None:
        curr = curr.next
        tail = tail.next.next
    head2 = curr.next
    curr.next = None
    if curr.next == None:
        return
    mergeSort(head1)
    mergeSort(head2)
    merge(head1,head2)

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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = mergeSort(l)
printll(l)

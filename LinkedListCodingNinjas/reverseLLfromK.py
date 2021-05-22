class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reversefromK(head, k):
    if head is None or head.next is None:
        return head
    prev = None
    next = None
    current = head
    count = 0
    while head is not None and count != k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    if next != None:
        head.next = reversefromK(next,k)
    return prev

def ll(arr):
    if len(arr) == 0:
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
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
k = int(input("Enter K "))
l = reversefromK(l,k)
printll(l)

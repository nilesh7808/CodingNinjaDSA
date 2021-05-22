class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge(head1,head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data >= head2.data:
        fhead = head2
        curr1 = head1
        curr2 = head2.next
    else:
        fhead = head1
        curr1 = head1.next
        curr2 = head2
    fcurr = fhead
    while curr1 and curr2:
        if curr1.data>=curr2.data:
            fcurr.next=curr2
            curr2=curr2.next
            fcurr=fcurr.next
        else:
            fcurr.next=curr1
            curr1=curr1.next
            fcurr=fcurr.next
    if curr1:
        fcurr.next=curr1
    if curr2:
        fcurr.next=curr2
    return fhead

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

# Main
# Read the link list elements including -1
arr1=list(int(i) for i in input().strip().split(' '))
arr2=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l1 = ll(arr1[:-1])
l2 = ll(arr2[:-1])
l = merge(l1, l2)
printll(l)
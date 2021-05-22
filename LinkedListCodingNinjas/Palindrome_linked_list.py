class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def check_palindrome(head):
    l= head
    prev = None
    while l.next:
        l.prev = prev
        prev = l
        l = l.next
    tail = l
    tail.prev = prev
    while head is not tail and head.data == tail.data:
        head = head.next
        tail = tail.prev
    if head is tail:
        return True
    elif head.data == tail.data:
        return True
    else:
        return False
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
ans = check_palindrome(l)
if ans:
    print("true")
else:
    print("false")



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def ithNode(head, i):
    current = head  # Initialise temp
    count = 0  # Index of current node
    while (current != None):
        if (count == i):
            return current
        count += 1
        current = current.next
    return
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

# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i=int(input())
node = ithNode(l, i)
if node:
    print(node.data)

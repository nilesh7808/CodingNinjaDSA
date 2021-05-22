class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def linearSearchRecursive(head, n):
    if head == None:
        return -1
    if head.data == n:
        return 0
    smallHead = linearSearchRecursive(head.next,n)
    if smallHead == -1:
        return -1
    else:
        return (1 + smallHead)
def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

from sys import setrecursionlimit

setrecursionlimit(11000)
arr = list(int(i) for i in input().strip().split(' '))
l = ll(arr[:-1])
data = int(input())
index = linearSearchRecursive(l, data)
print(index)

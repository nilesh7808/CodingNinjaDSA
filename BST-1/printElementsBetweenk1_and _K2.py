import queue
class BinaryNodeTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def elemnts_between_k1_and_K2(root, k1, k2):

    if root == None:
        return None

    if root.data > k1 :
        elemnts_between_k1_and_K2(root.left, k1, k2)

    elif root.data < k2:
        elemnts_between_k1_and_K2(root.right, k1, k2)

    else:

        elemnts_between_k1_and_K2(root.left, k1, k2)
        print(root.data,end=" ")
        elemnts_between_k1_and_K2(root.right, k1, k2)


def takeInput():
    q = queue.Queue()
    print("Enter Root:")
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryNodeTree(rootData)
    q.put(root)
    while (not(q.empty())):
        Current_Node = q.get()
        print("Enter Left child of", Current_Node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryNodeTree(leftChildData)
            Current_Node.left = leftChild
            q.put(leftChild)
        print("Enter Right child of", Current_Node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryNodeTree(rightChildData)
            Current_Node.left = rightChild
            q.put(rightChild)

    return root
root = takeInput()
k1, k2 = list(int (i) for i in input().strip().split())
elemnts_between_k1_and_K2(root, k1, k2)
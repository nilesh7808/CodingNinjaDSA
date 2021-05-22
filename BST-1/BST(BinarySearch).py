import queue
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def searchInBST(root, k):
    if root == None:
        return False

    if root.data == k:
        return True

    elif root.data > k:
        return searchInBST(root.left, k)

    else:
        return searchInBST(root.right, k)

def takeInput():
    q = queue.Queue()
    print("Enter Root:")
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    q.put(root)
    while (not(q.empty())):
        Current_Node = q.get()
        print("Enter Left Child of",Current_Node.data)
        leftRootData = int(input())
        if leftRootData != -1:
            leftChild = BinaryTree(leftRootData)
            Current_Node.left = leftChild
            q.put(leftChild)
        print("Enter right child of", Current_Node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTree(rightChildData)
            Current_Node.right = rightChild
            q.put(rightChild)
    return root


root = takeInput()
k = int(input("Enter K:"))
node = searchInBST(root, k)
if node:
    print("True")
else:
    print("False")
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def pathSumrootToLeaf(root, k, lst):
    if root == None:
        return 0
    leftSum = 0
    rightSum = 0
    if root.left != None:
        leftSum = pathSumrootToLeaf(root.left, k, lst)
    if root.right != None:
        rightSum = pathSumrootToLeaf(root.right, k, lst)

    if (root.data + leftSum + rightSum) == k:
        print(root.data, leftSum, rightSum)

def takeInput():
    q = queue.Queue()
    print("Enter Root:")
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTreeNode(rootData)
    q.put(root)
    while (not (q.empty())):
        current_Node = q.get()
        print("Enterv left Child of",current_Node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTreeNode(leftChildData)
            current_Node.left = leftChild
            q.put(leftChild)
        print("Enter Right Child of",current_Node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTreeNode(rightChildData)
            current_Node.right = rightChild
            q.put(rightChild)

    return root

root = takeInput()
k=int(input())
pathSumrootToLeaf(root, k, [])
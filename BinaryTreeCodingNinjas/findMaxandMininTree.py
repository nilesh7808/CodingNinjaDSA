import queue
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

INT_MIN = -2147483648
INT_MAX = 2147483647

def findMax(root):
    if root == None:
        return INT_MIN
    res = root.data
    lres = findMax(root.left)
    rres = findMax(root.right)
    if lres > res:
        res = lres
    if rres > res:
        res = rres
    return res

def findMin(root):
    if root == None:
        return INT_MAX

    res = root.data
    lres = findMin(root.left)
    rres = findMin(root.right)
    if lres < res:
        res = lres
    if rres < res:
        res = rres
    return res

def minMax(root):
    min = findMin(root)
    max = findMax(root)
    return min, max

def takeLevelWiseInput():
    q = queue.Queue()
    print("Enter root: ")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    q.put(root)
    while (not (q.empty())):
        curr_Node = q.get()
        print("Enter Left Node of ",curr_Node.data)
        leftNodeData = int(input())
        if leftNodeData != -1:
            leftNode = BinaryTree(leftNodeData)
            curr_Node.left = leftNode
            q.put(leftNode)
        print("Enter Right Node of ", curr_Node.data)
        rightNodeData = int(input())
        if rightNodeData != -1:
            rightNode = BinaryTree(rightNodeData)
            curr_Node.right = rightNode
            q.put(rightNode)
    return root

root = takeLevelWiseInput()
minimum, maximum = minMax(root)
print(maximum, minimum)

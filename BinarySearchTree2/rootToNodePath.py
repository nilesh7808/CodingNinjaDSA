import queue
class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToNode(root, x):
    if root== None:
        return None

    if root.data == x:
        l = list()
        l.append(root.data)
        return l
    leftOutput = rootToNode(root.left,x)
    if leftOutput != None:
        leftOutput.append(root.data)
        return leftOutput

    rightOutput = rootToNode(root.right, x)
    if rightOutput != None:
        rightOutput.append(root.data)
        return rightOutput

    else:
        return None

    pass

def takeInputLevel():
    q = queue.Queue()
    print("Enter Root: ")
    rootData = int(input())
    if rootData == -1:
        return None

    root = BinaryTree(rootData)
    q.put(root)
    while (not q.empty()):
        curr_Node= q.get()
        print("Enter Left Node of ",curr_Node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTree(leftChildData)
            curr_Node.left = leftChild
            q.put(leftChild)
        print("Enter Right child of: ",curr_Node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTree(rightChildData)
            curr_Node.right = rightChild
            q.put(rightChild)

    return root

root = takeInputLevel()
x = int(input())
print(rootToNode(root, x))


import queue
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printDetailed(root):
    if root == None:
        return
    print(root.data,end=" : ")
    if root.left != None:
        print("L",root.left.data,end=", ")
    if root.right != None:
        print("R",root.right.data,end=" ")
    print()
    printDetailed(root.left)
    printDetailed(root.right)

def takeInputLevelWise():
    q = queue.Queue()
    print("Enter Root ")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    q.put(root)
    while ((not q.empty())):
        curr_Node = q.get()
        print("Enter Left child of ",curr_Node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTree(leftChildData)
            curr_Node.left = leftChild
            q.put(leftChild)

        print("Enter Rightchild of ",curr_Node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTree(rightChildData)
            curr_Node.right = rightChild
            q.put(rightChild)
    return root

root = takeInputLevelWise()
printDetailed(root)
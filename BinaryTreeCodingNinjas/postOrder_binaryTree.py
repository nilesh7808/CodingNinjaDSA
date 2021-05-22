class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def postOrder(root):
    if root == None:
        return None
    postOrder(root.left)
    postOrder(root.right)
    print(root.data,end=" ")
def takeInpuut():
    rootData = int(input())
    if rootData == -1:
        return
    leftTree = takeInpuut()
    rightTree = takeInpuut()
    root = BinaryTree(rootData)
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInpuut()
postOrder(root)
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def in_Order(root):
    if root == None:
        return None
    in_Order(root.left)
    print(root.data,end=" ")
    in_Order(root.right)
def takeInpuut():
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    leftTree = takeInpuut()
    rightTree = takeInpuut()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInpuut()
in_Order(root)
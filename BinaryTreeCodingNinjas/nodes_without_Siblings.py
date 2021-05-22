class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def Nodes_Without_Siblings(root):
    if root == None:
        return
    Nodes_Without_Siblings(root.left)
    if root.left == None and root.right != None:
        print(root.right.data)
    if root.left != None and  root.right == None:
        print(root.left.data)
    Nodes_Without_Siblings(root.right)
def takeInput():
    rootData = int(input())
    if rootData == -1:
        return
    root = BinaryTree(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root

root = takeInput()
Nodes_Without_Siblings(root)
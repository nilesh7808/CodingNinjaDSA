class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def  replaceNodesDepth(root,k = 0):
    if root == None:
        return
    root.data = k
    replaceNodesDepth(root.left,k+1)
    replaceNodesDepth(root.right,k+1)
    return

def takeInput():
    rootData = int(input("Enter Data "))
    if rootData == -1:
         return
    root = BinaryTree(rootData)
    leftTree = takeInput()
    rightTree = takeInput()
    root.left = leftTree
    root.right = rightTree
    return root
root = takeInput()
replaceNodesDepth(root)
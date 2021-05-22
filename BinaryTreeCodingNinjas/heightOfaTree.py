class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    leftHeight = 0
    rightHeight = 0
    if root == None:
        return 0
    leftHeight += height(root.left)
    rightHeight += height(root.right)
    if leftHeight > rightHeight:
        return 1 +leftHeight
    return 1 + rightHeight
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
print(height(root))
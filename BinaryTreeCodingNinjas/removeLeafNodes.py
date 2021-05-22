class BinaryTree2:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def remove_leaf_nodes(root):

    if root == None:
        return None

    if root.left == None and root.right == None:
        return None

    print(root.data,end = " ")
    root.left = remove_leaf_nodes(root.left)
    root.right = remove_leaf_nodes(root.right)

def takeInput():

    rootData = int(input())
    if rootData == -1:
        return

    root = BinaryTree2(rootData)

    leftTree = takeInput()
    rightTree = takeInput()

    root.left = leftTree
    root.right = rightTree

    return root

root = takeInput()
remove_leaf_nodes(root)

class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printDetailedTree(root):
    if root == None:
        return None
    print(root.data ,end=": ")
    if root.left != None:
        print("L: ",root.left.data,end=", ")
    if root.right != None:
        print("R: ",root.right.data,end="")
    print()

    printDetailedTree(root.left)
    printDetailedTree(root.right)
    return root

def buildTreeInorPost(inorder,postorder):
    if len(postorder) == 0:
        return None

    rootData = postorder[len(postorder)-1]
    root = BinaryTree(rootData)
    rootIndexinInorder = -1
    for i in range(0,len(inorder)):
        if inorder[i] == rootData:
            rootIndexinInorder = i
            break
    if rootIndexinInorder == -1:
        return None


    leftinorder = inorder[0:rootIndexinInorder]
    rightinorder = inorder[rootIndexinInorder+1:]

    lenleftsubtree = len(leftinorder)

    leftpostorder = postorder[0:lenleftsubtree]
    rightpostorder = postorder[lenleftsubtree:len(postorder)-1]

    leftchild = buildTreeInorPost(leftinorder,leftpostorder)
    rightChild = buildTreeInorPost(rightinorder,rightpostorder)

    root.left = leftchild
    root.right = rightChild
    return root
inorder = [4,2,5,1,6,3,7]
postorder = [4,5,2,6,7,3,1]
root = buildTreeInorPost(inorder,postorder)
printDetailedTree(root)
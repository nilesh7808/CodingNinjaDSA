class GenericTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def printTree(root):

    #not a base case but an edge case
    if root == None:
        return
    print(root.data, end=" ")
    for child in root.children:
        printTree(child)

def printTreeDetailed(root):

    if root == None:
        return

    print(root.data,":",end=" ")

    for child in root.children:
        print(child.data,",",end="")
    print()

    for child in root.children:
        printTreeDetailed(child)

def countNodes(root):
    if root == None:
        return 0
    count = 1
    for child in root.children:
        count = count + countNodes(child)
    return count

def takeTreeInput():
    print("Enter the root node:-")
    rootData = int(input())

    if rootData == -1:
        return None
    root = GenericTreeNode(rootData)
    print("Enter number of children of",rootData)
    childrencount = int(input())
    for i in range(childrencount):
        child = takeTreeInput()
        root.children.append(child)
    return root

root = takeTreeInput()
print(countNodes(root))
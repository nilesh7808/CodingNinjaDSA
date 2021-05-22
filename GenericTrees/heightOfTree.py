class GenericTrees:
    def __init__(self, data):
        self.data = data
        self.children = list()

def heightTree(root):
    if root == None:
        return 0
    h = 0
    for child in root.children:
        if h < heightTree(child):
            h = heightTree(child)
    return h + 1

def takeTreeInput():
    print("Enter Root Node:-")
    rootData = int(input())
    if rootData == -1:
        return None
    root = GenericTrees(rootData)
    print("Enter number of nodes for", rootData)
    numberChild = int(input())
    for i in range(numberChild):
        child = takeTreeInput()
        root.children.append(child)
    return root

root = takeTreeInput()
print(heightTree(root))
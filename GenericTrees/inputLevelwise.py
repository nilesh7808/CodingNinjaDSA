import queue
class GenericTrees:
    def __init__(self, data):
        self.data = data
        self.children = list()

def printLevelWiseTree(root):
    if root == None:
        return
    print(root.data,":",end=" ")
    for child in root.children:
        print(child.data,",",end=" ")
    print()
    for child in root.children:
        printLevelWiseTree(child)

def takeLevelWiseInput():
    q = queue.Queue()
    print("Enter Root Node:-")
    rootData = int(input())
    if rootData == -1:
        return None
    root = GenericTrees(rootData)
    q.put(root)
    while(not(q.empty())):
        curr_Node = q.get()
        print("Enter the number of child for", curr_Node.data)
        numchild = int(input())
        for i in range(numchild):
            print("Enter the next child for",root.data)
            childData = int(input())
            child = GenericTrees(childData)
            curr_Node.children.append(child)
            q.put(child)
    return root
root = takeLevelWiseInput()
printLevelWiseTree(root)

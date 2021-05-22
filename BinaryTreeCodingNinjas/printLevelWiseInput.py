import queue
class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printLevelwiseInput(root):

    import queue
    q = queue.Queue()
    if root == None:
        return None
    q.put(root)

    while (not(q.empty())):
        a = q.get()
        print(a.data, end=": ")

        leftChild = a.left
        if leftChild != None:
            print("L ", end=" ")
            print(leftChild.data,end=" , ")
            q.put(leftChild)

        rightChild = a.right
        if rightChild != None:
            print("R ", end=" ")
            print(rightChild.data)
            q.put(rightChild)
        else:
            print("R:", end="")
            print(-1)
        return root


def takeLevelwiseInput():
    q = queue.Queue()
    print("Enter Root ")
    rootData = int(input())
    if rootData == -1:
        return None
    root = BinaryTree(rootData)
    q.put(root)
    while (not (q.empty())):
        curr_Node = q.get()
        print("Enter Left Node of",curr_Node.data)
        leftChildData = int(input())
        if leftChildData != -1:
            leftChild = BinaryTree(leftChildData)
            curr_Node.left = leftChild
            q.put(leftChild)
            
        print("Enter Right Node of",curr_Node.data)
        rightChildData = int(input())
        if rightChildData != -1:
            rightChild = BinaryTree(rightChildData)
            curr_Node.right = rightChild
            q.put(rightChild)

    return root

root = takeLevelwiseInput()
printLevelwiseInput(root)
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def longestPathHelper(root, string = ""):
    if root == None:
        return ""
    if root.left == root.right and root.left == None:
        return str(root.data) + " "
    if root.left != None:
        stringL = longestPathHelper(root.left, string)
    if root.right != None:
        stringR = longestPathHelper(root.right, string)
        
    if root.left == None:
        return stringR + str(root.data) + " "
    elif root.right == None:
        return stringL + str(root.data) + " "
    else:
        if len(stringL) > len(stringR):
            string = stringL
        else:
            string = stringR
            
    return string + str(root.data) + " "

def longestPath(root):
    string = longestPathHelper(root)
    return string.split()

    

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
path = longestPath(root)
for ele in path:
    print(ele)

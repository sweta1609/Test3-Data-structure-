import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None
class NodeInfo:
    def __init__(self, key, level, parent):
        self.key = key
        self.level = level
        self.parent = parent
 
def inorder(root, parent, level, x, y):
 
    if root is None:
        return
 
    inorder(root.left, root, level + 1, x, y)
    if root.key == x.key:
        x.level = level
        x.parent = parent

    if root.key == y.key:
        y.level = level
        y.parent = parent
 
    inorder(root.right, root, level + 1, x, y)
 
 
def checkCousins(root, elem1, elem2):
 
    if root is None:
        return False
 
    level = 1           
    parent = None       
 
    x = NodeInfo(elem1, level, parent)
    y = NodeInfo(elem2, level, parent)
 
    inorder(root, None, 1, x, y)
 
    if x.level != y.level or x.parent == y.parent:
        return False
 
    return True
 
   

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
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans is True:
    print('true')
else:
    print('false')

class treeNode:
    data=0
    left=None
    right=None
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def getData(self):
        return self.data



def InsertHelper(root,data):
    if(root==None):
        newNode=treeNode(data)
        return newNode
    if data>=root.getData():
       root.right= InsertHelper(root.right,data)
    else:
       root.left= InsertHelper(root.left,data)
    return root

def PrintHelper(myRoot):
    if myRoot == None:
        return
    print(myRoot.data)
    PrintHelper(myRoot.left)
    PrintHelper(myRoot.right)



class BST:
    def __init__(self):
        self.root=None

    def PrintHelper(self,myRoot):
        if myRoot == None:
            return
        print(myRoot.data)
        PrintHelper(myRoot.left)
        PrintHelper(myRoot.right)

    '''def InsertHelper(self,myRoot, data):
        if (myRoot == None):
            newRoot = treeNode(data)
            return newRoot
        if data >= myRoot.getData():
            myRoot = InsertHelper(myRoot.right, data)
            return myRoot
        else:
            myRoot = InsertHelper(myRoot.left, data)
            return myRoot
            '''

    def Insert(self, data):
        self.root = InsertHelper(self.root, data)

    def PrintTree(self):
        PrintHelper(self.root)#check from here. I was last here

myTree=BST()
myTree.Insert(10)
myTree.Insert(20)
myTree.Insert(5)
myTree.Insert(90)
myTree.PrintTree()
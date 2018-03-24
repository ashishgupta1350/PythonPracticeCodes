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
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def setLeft(self,newLeft):
        self.left=newleft
    def setRight(self,newRight):
        self.right=newRight

def InsertHelper(root,data):
    if(root==None):
        newNode=treeNode(data)
        return newNode
    if data>=root.getData():
       root.right=InsertHelper(root.right,data)
    else:
       root.left= InsertHelper(root.left,data)
    return root

def PrintHelper(myRoot):
    if myRoot == None:
        return
    print(myRoot.getData())
    print(myRoot.data,end=" ")
    PrintHelper(myRoot.left)
    PrintHelper(myRoot.right)

def preOrder(myRoot):
    if myRoot==None:
        return
    print(myRoot.data,end=" ")
    inOrder(myRoot.left)
    inOrder(myRoot.right)

def inOrder(myRoot):
    if myRoot==None:
        return

    inOrder(myRoot.left)
    print(myRoot.data,end=" ")
    inOrder(myRoot.right)

def postOrder(myRoot):
    if myRoot == None:
        return
    inOrder(myRoot.left)
    inOrder(myRoot.right)
    print(myRoot.data,end=" ")


class BST:
    def __init__(self):
        self.root=None
        
    def Insert(self, data):

        if self.root==None:
            newNode=treeNode(data)
            self.root=newNode

        InsertHelper(self.root, data)
        print(self.root, self.root.right)
    def PrintTree(self):
        PrintHelper(self.root)#check from here. I was last here
        print('')
    def PostOrderPrint(self):
        postOrder(self.root)
        print('')
    def PreOrderPrint(self):
        preOrder(self.root)
        print('')
    def InOrderPrint(self):
        inOrder(self.root)
        print('')


myTree=BST()
myTree.Insert(10)
myTree.Insert(20)
myTree.Insert(5)
myTree.Insert(20)
myTree.Insert(100)

myTree.PrintTree()
myTree.InOrderPrint()
myTree.PreOrderPrint()
myTree.PostOrderPrint()

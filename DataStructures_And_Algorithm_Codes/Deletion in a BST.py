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


def deleteHelper(root,data):
    if root==None:
        return
    if root.getData()==data:
        if root.left==None:
            return root.right
        elif root.right==None:
            return root.left
        else:
            temp=root.left
            while temp.right:
                temp=temp.right
            #swapping
            x=root.data
            root.data=temp.data
            temp.data=x
            root.left=deleteHelper(root.left,temp.data)
            return root

    else:
        if root.getData()<data:
           root.right= deleteHelper(root.right,data)
        else:
            root.left=deleteHelper(root.left,data)


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
    print(myRoot.data,end=", ")
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

  

    def Insert(self, data):
        self.root = InsertHelper(self.root, data)

    def PrintTree(self):
        PrintHelper(self.root)#check from here. I was last here
        print('')

    def deleteElement(self,data):
        if self.root==None:
            print('UnderFlow')
            return
        self.root=deleteHelper(self.root,data)

myTree=BST()
myTree.Insert(10)
myTree.Insert(20)
myTree.Insert(5)
myTree.Insert(90)

myTree.PrintTree()

myTree.deleteElement(10)

myTree.PrintTree()


myTree.PrintTree()

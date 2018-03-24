class Node:

    def __init__(self,data=None,next=None,prev=None):
        self.data=data
        self.next=next
        self.prev=prev

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self,newNext):
        self.next=newNext

    def setPrev(self,newPrev):
        self.prev=newPrev

    def getPrev(self):
        return self.prev

class stack:
    def __init__(self):
        self.size=0
        self.head=None

    def top(self):
        if self.head==None:
            print('Stack is empty.')
            return
        return self.head.getData()

    def pop(self):
        if self.head==None:
            print('Stack is empty.')
            return

    def push(self,data):
        newNode=Node(data)
        if self.head==None:
            self.head=newNode
            return
        newNode.setNext(self.head)
        self.head=newNode

    def print(self):
        current=self.head
        while current:
            print(current.getData(),end=" " )
            current=current.getNext()
        print('')

    def isEmpty(self):
        if(self.head==None):
            return True
        return False

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)


myStack=stack()
myStack.push(10)
myStack.push(20)
myStack.push(100)
myStack.push(40)
myStack.push(30)
print('Top element of stack is : ',myStack.top())
myStack.pop()
print('printing whole stack : ')
myStack.print()
myStack.pop()
myStack.top()
if myStack.isEmpty()==True:
    print('Stack is empty')
else:
    print('Stack is non empty')

print('Start of Queues part')

q=Queue()

q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
q.print()


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

class doublyLL:
    def __init__(self, head=None):
        self.head = head

    def Insert(self,data): #the given program inserts at the front of the doubly linked list
        if self.head==None:
            newNode=Node(data)
            self.head=newNode
            return
        newNode=Node(data)
        newNode.setNext(self.head)
        self.head.setPrev(newNode)
        self.head=newNode
        return

    def Size(self):
        current=self.head
        count=0
        while current:
            count=count+1
            current=current.getNext()
        return count
    def Print(self):
        current=self.head
        while current:
            print(current.getData(),end=" ")
            current=current.getNext()

    def PrintReverse(self):
        current=self.head
        while current:
            current=current.getNext()
        while current:
            print(current.getData(), end=" ")
            current=current.getPrev()
        print('')
        return

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
        if current is None:
            print('Not found %d in list' %(data))
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
        if current is None:
            print('Data Not in List')
            return
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            current=current.setNext()
            current.setPrev(previous)

List=doublyLL()
List.Insert(100)
List.Insert(40)
List.Insert(30)
List.Insert(90)
List.Insert(25)
List.Insert(75)
List.Print()
List.PrintReverse()
List.delete(75)
List.delete(25)
print('List after deletion : ',end=" ")
List.Print()
print('')
print('Deleting 2 which is not in list : ',end=" ")
List.delete(2)#no such element in the doubly LL
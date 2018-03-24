class Node:

    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self,newNext):
        self.next=newNext

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def Insert(self,data):

        newNode=Node(data)
        newNode.setNext(self.head)
        self.head=newNode

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

List=LinkedList()
List.Insert(10)
List.Insert(50)
List.Insert(30)
List.Insert(100)
List.Insert(20)
List.Print()
List.delete(10)
List.delete(100)
print('')
List.Print()
import sys
import random
import os

class myQueue:
    __myList=[None]*5
    __front=int(0)
    __rear=int(0)
    __numElements=int(0)
    __sizeofQueue=int(0)

    def __init__(self,Size):
        self.____myList=[None]*Size
        self.____numElements=int(0)
        self.____sizeofQueue=Size
        self.____front = int(0)
        self.____rear = int(0)


    def enqueue(self,element):
        self.__sizeofQueue=5
        if(self.__sizeofQueue==self.__numElements):
            print('OverFlow')
            return
        self.__numElements+=1
        self.__myList[self.__rear]=element
        self.__rear+=1
        self.__rear%=self.__sizeofQueue


    def dequeue(self):
        if(self.__numElements==0):
            print('UnderFlow')
            return
        self.__numElements-=1
        self.__front+=1
        self.__front%=self.__sizeofQueue


    def traverse(self):

        if(self.__front>=self.__rear):
            for i in range (self.__front,self.__sizeofQueue):
                print(self.__myList[i],end=" ")
            for i in range(self.__rear, self.__front):
                print(self.__myList[i], end=" ")
        else:
            for i in range(self.__front,self.__rear):
                print(self.__myList[i],end=" ")


    def countElements(self):
        return self.__numElements


q=myQueue(5)
q.enqueue(10)
q.enqueue(90)
q.enqueue(60)
q.enqueue(30)
q.enqueue(40)
q.traverse()
q.enqueue(20)
q.dequeue()
q.dequeue()
q.dequeue()
q.enqueue(90)
q.enqueue(60)
q.enqueue(30)
q.traverse()



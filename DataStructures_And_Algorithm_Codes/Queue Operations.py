import sys
import random
import os

class myQueue:
    __myList=[]
    __numElements=int(0)

    def __init__(self):
        __myList=[]
        __numElements=int(0)

    def enqueue(self,element):

        self.__myList.append(element)
        self.__numElements+=1

    def dequeue(self):
        if(self.__numElements==0):
            print('UnderFlow')
            return

        del(self.__myList[0]) #check for errors
        self.__numElements -=1

    def printQueue(self):
        print(self.__myList)

    def countElements(self):
        return self.__numElements


queue=myQueue()
queue.enqueue(20)
queue.enqueue(40)
queue.enqueue(30)
queue.enqueue(10)

queue.printQueue()

queue.dequeue()
queue.dequeue()

queue.printQueue()

queue.enqueue(100)

queue.printQueue()


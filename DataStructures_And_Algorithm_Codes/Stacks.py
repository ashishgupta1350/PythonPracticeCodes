import random
import sys
import os

class stack:
    __myList=[]
    __numElements=0

    def __init__(self):
        __myList=[]
        __numElements=0

    def Push(self, element):
        self.__myList.append(element)
        self.__numElements+=1

    def Pop(self):
        if(self.__numElements>0):
            self.__myList.pop()
            self__numElements=self.__numElements -1


    def printStack(self):
        print(self.__myList)

    def numElements(self):
        return __numElements

    def get_type(self):
        print('stack')


s=stack()
s.Push(10)
s.printStack()
s.Push(20)
s.Push(30)
s.printStack()
s.Pop()
s.printStack()
s.Pop()
s.printStack()
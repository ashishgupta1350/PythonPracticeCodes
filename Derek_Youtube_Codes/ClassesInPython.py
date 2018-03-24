import random
import sys
import os

class Animal:
    __name=""
    __height=0
    __weight=0
    __sound=0

    def setName( self,name):
        self.__name=name
        
    def getName(self):
        return self.__name

myAnimal=Animal()
myAnimal.setName("Dog")
print(myAnimal.getName())


class Stack:

    __list=[]
    __listSize=0
   

    def __init__(self,listOfNumbers):
        self.__numElements=len(listOfNumbers)
        
        __listSize=len(self.__list)
        
    def Pop(self):
        
        self.__list.pop()
        __listSize=len(self.__list)
        

    def Push(self,data):
        self.__list.append(data)
        __listSize=len(self.__list)
'''
    def getSize(self):
        return self.__listSize

    def getTop(self):
        return self.__list(len(self.__list)-1)
   '''


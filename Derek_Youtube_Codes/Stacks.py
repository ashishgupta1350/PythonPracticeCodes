class Stack:
    __list=[]
    __listSize=0
   

    def __init__(self,listOfNumbers):
        self.__listSize=len(listOfNumbers)
        #self.__list=listOfNumbers
        __listSize=len(self.__list)
        
    def Pop(self):
        
        self.__list.pop()
        __listSize=len(self.__list)
        

    def Push(self,data):
        self.__list.append(data)
        __listSize=len(self.__list)

    def getSize(self):
        return self.__listSize

    def getTop(self):
        return self.__list(len(self.__list)-1)



myTuple=tuple(1,2,3,4,5,6,7,8,9)

myList=list(myTuple)

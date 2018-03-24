import sys
import random
import os

def checkBalanced(myString):
    myStack=list()
    flag=0
    for i in range(0 , len(myString)):
        
        if(myString[i]=='{' or myString[i]=='(' or myString[i]=='<' or myString[i]=='[' ):
           
            myStack.append(myString[i])

        elif myString[i]=='}':
            if  len(myStack)!=0 and myStack[len(myStack)-1]=='{' and len(myStack)!=0:
                myStack.pop()
                continue
            else :
                return False
        elif myString[i]=='>':
            if len(myStack)!=0 and  myStack[len(myStack)-1]=='<'and len(myStack)!=0:
                myStack.pop()
                continue
            else :
                return False

        elif myString[i]==')':
            if len(myStack)!=0 and  myStack[len(myStack)-1]=='(' and len(myStack)!=0:
                myStack.pop()
                continue
            else :
                return False
        elif myString[i]==']':
            if len(myStack)!=0 and  myStack[len(myStack)-1]=='[' and len(myStack)!=0:
                myStack.pop()
                continue
            else :
                return False


myString='a+(b+c)-d*<e+f>'
if(checkBalanced(myString)==False):
    print('Not Balanced')
else :print('Balanced')
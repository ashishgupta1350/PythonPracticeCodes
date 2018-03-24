import random
import sys
import os

testFile=open("test.txt","wb")
print(testFile.mode,'\n')
print(testFile.name,'\n')
testFile.write(bytes("Lets Write to file\n",'UTF-8'))
testFile.close()
testFile=open("test.txt","r+")
testFileData=testFile.read()
print(testFileData)
testFile.close()
os.remove("test.txt")

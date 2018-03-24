myList=[]
num=int(input('Enter the number of elements in the array '))
print('Enter array')
for i in range(0,num):
    myList.append(int(input('')))
print(myList)
Insert=int(input('Enter number to insert'))
Index=int(input('Enter index'))

if(Index>num):
    print('Not in range')
elif Index<0:
    print('Not a valid index')
else:
    myList.insert(Insert,Index)

print(myList)

num=num+1
Index=int(input('Enter index at which you want to perform deletion '))

if(Index>=num):
    print('Not in range')
elif Index<0:
    print('Not a valid index')
else:
    myList.remove(Index)

print(myList)
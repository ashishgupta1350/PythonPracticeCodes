def bubblesort(myList,num):
    for i in range(0,num):
        for j in range(i,num):
            if(myList[i]>myList[j]):
                temp=myList[i]
                myList[i]=myList[j]
                myList[j]=temp
    return



myList=[]

num=int(input('Enter the number of elements in the array '))
print('Enter array')
for i in range(0,num):
    myList.append(int(input('')))

print(myList)

bubblesort(myList,num)

print(myList)
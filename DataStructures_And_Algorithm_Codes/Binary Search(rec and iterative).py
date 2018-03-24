def binarySearchRecursive(myList,element,start,end):
    #base case
    if(start>end): return False

    mid=int((start+end)/2)

    if myList[mid]==element:
        return True
    elif(myList[mid]>element):
        return binarySearchRecursive(myList,element,start,mid-1)
    else:
       return binarySearchRecursive(myList, element, mid+1, end)

    #the recursive case

def binarySearchIterative(myList,element,num):
    start=0
    end=num
    while start<=end:
        mid=int((start+end)/2)
        if myList[mid] == element:
            return True
        elif (myList[mid] > element):
            end=mid-1
        else:
            start=mid+1
    return False

myList=[]
num=int(input('Enter the number of elements in the array '))
print('Enter array')
for i in range(0,num):
    myList.append(int(input('')))
print(myList)
# my list has been printed here
myList.sort()
element=int(input('Enter Element to Search: '))
if(binarySearchRecursive(myList,element,int(0),int(num))==True):
    print('Yes, It exists')
else:
    print('No, It does not Exist')

if(binarySearchIterative(myList,element,num)==True):
    print('Yes, It exists')
else:
    print('No, It does not Exist')


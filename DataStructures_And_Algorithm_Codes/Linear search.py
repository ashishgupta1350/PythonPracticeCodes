myList=[]

num=int(input('Enter the number of elements in the array '))
print('Enter array')
for i in range(0,num):
    myList.append(int(input('')))
print(myList)
search=int(input('Enter number to search'))
flag=int(0)
for x in myList:
    if x==search:
        print('found')
        flag=1
        break

if(flag==0):
    print('not found')
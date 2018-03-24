import random
import sys
import os
value = 3
temp=['Help','MyPython']
grocery_list=['Juice','Tomatoes','Oranges','PineApples']

print (grocery_list)

print(grocery_list[1])

grocery_list.append('Onions')
grocery_list.remove('Juice')
print(grocery_list)
grocery_list.sort()
print(grocery_list)
grocery_list.reverse()
del grocery_list[2];
print(grocery_list)
grocery_list+=temp
print(grocery_list)
print(max(grocery_list))
print(min(grocery_list))
print(len(grocery_list))

grocery_list.pop()

print(grocery_list)



import random
import sys
import os

pi_tuple=(3,4,5,6,7,8)
print pi_tuple
new_tuple=list(pi_tuple)
new_tuple.reverse()

new_List=tuple(new_tuple)
print new_List

age=12

if age>20 :
    print You are above 20
elif (age>10) and (age<=20):
    print Not above 20
else :
    print Is today someones birthday?

for x in range(0,10):
    print x;
print('\n')

grocery_list=['Juice','bananas','potatoes']

for y in grocery_list:
    print (y)

for x in [2,4,5,6,7]:
    print(x, end=" ")
print('\n')

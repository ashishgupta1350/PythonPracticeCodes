import random
import os

print('Press : 1 for the standard dice, 2 for custom range dice')
choice=0;
choice=int(input('Your Choice : '))
while(1):
        
    if choice==1 :
        num=random.randint(1,6);
        print('Num is ',num);

    else:
        x=0
        y=0 
        x=int(input('Input Start of Range : '))
        y=int(input('Input end of Range : '))
        print('Num is ',random.randint(x,y))

    cont=int(input('Do you want to roll again? Press 1 for Yes and any other number for No! : '))
    if cont==1:  
        print('\n'*50) 
        continue
    else :
        break
print('End of Program')

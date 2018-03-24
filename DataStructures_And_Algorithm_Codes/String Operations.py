
def mySubstring(string4,index1,index2):
    for i in range(index1,index2+1):
        print(string4[i],end="")

string1='Hello, I am Ashish.'
string2='I have not copied any practical in this file.'
string3='Hello Ashish, Great'

#Length of the string :

print('Length of the string 1 is : ', len(string1))

# lets concatinate
print('Concatinated string is : ')
string4=string1+string2
print(string4)

#substring
index1=10
index2=20
#lets find the substring in string 4
print('Substring is : ')
mySubstring(string4,index1,index2)


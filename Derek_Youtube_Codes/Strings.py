import random
import sys
import os

print('What is your name?')

name = sys.stdin.readline()

print ('Hello ',name)

longString="Hello Python"

print(longString[0:5])
print(longString[-6:])
print(longString[:])
print("%c is my %s character and %d is my best number and %.5f is decimal"%
      ('C','favorite',1,.5))



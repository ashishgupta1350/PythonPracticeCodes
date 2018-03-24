import random
import sys
import os

# how do we declare strings

to_do_list=['to wash car', ' to run', ' go to college']
print(to_do_list)
to_do_list.append('hello')
print(len(to_do_list))
print('first item', to_do_list[0])
del(to_do_list[1:3])
to_do_list.insert(2,"send money")
to_do_list.sort()
print(to_do_list)
to_do_list.reverse()

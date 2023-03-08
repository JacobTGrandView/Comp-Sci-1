# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 14:09:12 2020

@author: jt108
"""

"""
def sum(total, val):
    
    print("sum is ", total)
    
    total = total + val
    
    input() #pause code execution
    
    sum(total, val + 1)
    
sum(0, 1)
"""



import random

def random_list(num_items, a, b):
    
    i = 0
    rlist = []
    
    while(i < num_items):
        x = random.randint(a, b)
        
        rlist.append(x)
        
        i = i + 1
        
    return rlist

nitems = int(input("size of list ? "))
a = int(input("lower limit - "))
b = int(input("upper limit - "))

list = random_list(nitems, a, b)

print(list)





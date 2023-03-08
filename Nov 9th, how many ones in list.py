# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 14:03:39 2020

@author: jt108
"""

#finding how many ones are in the list

myarray = [0, 1, 0, 1, 1, 0, 1, 0, 1]

num1 = 0

for item in myarray:
    num1 = num1 + item
    
print("number of 1s = ", num1)

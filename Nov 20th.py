# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:19:34 2020

@author: jt108
"""

def check_key(list, key):
    
    for item in list:
        if(item == key):
            print("item found")
            break
    
list1 = [34,12,45,67,-9]
key1 = 12

check_key(list1, key1)
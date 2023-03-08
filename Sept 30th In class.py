# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:02:41 2020

@author: jt108
"""

x = 0.0

for i in range(10):
    x = x + 0.1
    
if( abs(x - 1.0) < 0.0001):
    print("x is 1.0")
else:
    print("x is not 1.0")
    
    
    
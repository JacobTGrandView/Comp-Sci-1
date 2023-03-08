# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:18:39 2020

@author: jt108
"""

import math

            #a #b #c
def  sqroot(f, g, h):
    
    d = g ** 2 - 4 * f * h
    
    if(d < 0):
        print("there exists no real roots!")
    else:
        
        root1 = -g + math.sqrt(d)/(2 * f)
        root2 = (-g - math.sqrt(d))/(2 * f)
        
        print("root1 = ", root1, "root2 = ", root2)
        
        
a = int(input("enter a - "))
b = int(input("enter b - "))
c = int(input("enter c - "))

sqroot(a, b, c)



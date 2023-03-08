# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:20:28 2020

@author: jt108
"""

"""

def return_95():
    return 95

c = return_95()

print("c = ", c)

"""

"""

def return_pi():
    return 3.14

r = float(input(" r = "))

area = return_pi() * (r ** 2)

print("area of circle = ", area)

"""

"""

def return_var():
    
    c = 8
    return c #contents of variable c = 8

b = return_var() + 6

print("b is = ", b)

"""

"""
def mean(list):
    
    sum = 0
    
    for item in list:
        sum = sum + item
        
    mean = sum/len(list)
    
    return mean

list1 = [1,2,3,4,5]

x = mean(list1)

print("mean is = ", x)

"""


def compute_average(list1):
    
    total = 0
    
    for item in list1:
        total = total + item
        
    compute_average = total / len(list1)
    
    return compute_average

list1 = [ 1.1, 2.2, 3.3, 4.4, 5.5 ] 

a = compute_average(list1)

print("average is = ", a)
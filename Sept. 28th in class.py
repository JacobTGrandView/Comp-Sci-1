# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:16:44 2020

@author: jt108
"""

# the variable i is going to take the values
#provided by the range function
# the value provided the range function is copied into
# variable i

totalscore = 0

for i in range (0, 7): #0, 1, 2, 3, 4, 5, 6

    if(i == 2 or i == 4):
        pass
    else:
        print("Student ", i)
        score = int(input("enter your score of student : "))
        totalscore = totalscore + score
    
print("total score is ", totalscore)


print("welcome ", end='')
print("to the class")



"""
for i in range(0,5):
    for j in range(0,5): #row in the matrix
        print(j, end='')
    print("/n", end='') #print a new line
    
   """ 
    
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:10:53 2020

@author: jt108
"""



def remove_duplicate(list):
    
    NewList = []
    
    for item in list:
        
        if(not(item in NewList)):
            NewList.append(item)
            
    print(NewList)
    
nlist = [1,2,2,1,1,3,4,2,1,5,6,3,7]
    
remove_duplicate(nlist)









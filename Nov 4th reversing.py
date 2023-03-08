# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:42:13 2020

@author: jt108
"""

name = "tom hanks"

reverse_name = ''


print(name)

i = 0

while(i < len(name)):
  print(name[i])
  
  i = i + 1

  #this also works down below

  for char in name:
    print(char)



"""
numchars = len(name)

while(numchars > 0):

    reverse_name = reverse_name + name[numchars - 1]

#reverse_name = 's' + 'k' = 'sk'

numchars = numchars - 1

print(reverse_name)
"""
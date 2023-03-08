# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 19:09:42 2020

@author: Jacob Thomas
#Date of last revision: November 16th 2020
    
"""


"""
#########
#
#Problem A. Using a while loop to print each month in a year
#
#########


i = 0

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


while(i < 12): #12 months in a year, it stops at 12
    print(months[i])
    i = i + 1 #adds 1 to the month
"""



########
#
#Problem B. Using a for loop to print each month in a year.
#
########

"""

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for i in range(12): #12 months in a year
    print(months[i]) 
    i = i + 1 #adding 1 to the list 

"""

########
#
#Problem C. User inputs odd numbers and they will be saved to a list. When "done" is entered it stops and prints
#
########

"""

OddList = [] #empty list

while(True): #infinite loop until 'done' is entered
  inp = input("Enter an odd number or done: ") #input

  if(inp) == ("done"):
          break #Stops code
          
  NumInp = inp #setting variable to what user is inputting
  OddList.append(NumInp) #adding that to the empty list

print(OddList)

"""



#######
#
#Problem D. User inputs numbers into an empty list. The sum of the odd numbers will be printed
#
#######

"""

list = [] #empty list

OddSum = 0

while(True): #infinite loop
    inp = input("enter a number: ")
    
    if(inp == 'done'): #stop function
        print("Sum of odd numbers is : ", OddSum)
        break #stop
        
    inp_int = int(inp) #input is a string variable and making it an integer variable
        
    if(inp_int%2 == 1): #if number is odd
        OddSum = OddSum + inp_int #total of odd numbers
            
"""   
    
#######
#
#Problem E.  User can input any type of data and it will be concatenated together and printed
#
#######

MyList = [] #empty list

while(True): #infinite loop until 'done' is entered
  inp = input("Enter anything: ") #input
  MyList.append(inp) #adding whatever is input to the list

  if(inp) == ("done"):
        break #Stops code
        
string = '' #empty string
for item in MyList: 
    string += item #adds and shows results

print(string)
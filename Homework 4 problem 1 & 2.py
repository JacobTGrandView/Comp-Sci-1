#############Problem 1
"""

def num2month(monthlist):

    k = int(input("enter the month number - "))
    
    if(k > 12 or k < 1):
        print("enter a number between 1 and 12")
    else:
        print("month is ", monthlist[k - 1])

########### Main code ##########

#list of months
mlist = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul',
         'aug', 'sep', 'oct', 'nov', 'dec']

num2month(mlist) # call function and send mlist as argument

"""
########## Problem 2


def listproduct(list):
    
    product = 1
    
    for item in list:
        #before multiplying item,
        #we can check if the item is int or float type
        #type() function will tell us if the argument
        #is int or float
        if(type(item) == int or type(item) == float):
            product = product * item
    
    print("product is - ", product)

######## Main code ##########

#list of items need not be all numbers
list = [1, 2.2, 3, 'c', 'hello', '4.5']

listproduct(list)
    
   
    
    
        
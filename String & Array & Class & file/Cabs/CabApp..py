# -*- coding: utf-8 -*-

"""
 I imported cabs.py file. I found the number of lines first in the readfile function. 
 then I added an empty list to the list by separating the files with ":". 
 In the findequal function, I assigned the typeofcab and kms values of the object to the variables. 
 I found the length of the list for the loop. 
 With a double-incrementing for loop, where kms and typeofcab are the same, 
 increment the result variable by 1 and return the variable result after the for loop
 
"""

import cabs

def read_file(fname):
    ggwp = open(fname,"r")
    gg = ggwp.readlines()
    countoflines = len(gg)
    
    listofcabs = []
    f = open(fname, "r")
    for i in range(countoflines):
        x = f.readline()
        y = x[:len(x)-1].split(":")
        listofcabs += y
    return listofcabs


def find_equal(listofcabs,object):
    
    typeofcab=object.getType()
    kms = object.getKms
    countoflines = len(listofcabs)
    
    result = 0
    for i in range(1,countoflines,2):
        if(int(listofcabs[i])==kms and listofcabs[i-1]==typeofcab):
           result+=1
    
    return result








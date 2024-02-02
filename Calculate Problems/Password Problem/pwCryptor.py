#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 13:45:51 2021

"""

'''
There should not be 3 characters in a row next to each other and
should not contain birth year
'''

def is_spaced(password,indx=0):
    
    if(indx+2 == len(password)):
        return True
    else:
        if(abs(ord(password[indx+1]) - ord(password[indx])) != abs(ord(password[indx+2]) - ord(password[indx+1]))):
            return True and is_spaced(password,indx+1)
        else:
            return False


def contains_birthyear(password,birth):
    a = password[0:].find(birth[0])
    b = a + 1 + password[a+1:].find(birth[1])
    c = b + 1 + password[b+1:].find(birth[2])
    d = c + 1 + password[c+1:].find(birth[3])
    if(a<b<c<d):
        return True
    else:
        return False
    
def is_valid_password(password,birth):
    
    if(len(password)>=3 and is_spaced(password) and contains_birthyear(password,birth)==False):
        return True
    else:
        return False


while(True):
    
    password = str(input("Enter password: "))
    birth = str(input("Enter year of birth: "))
    
    if(is_valid_password(password, birth)):
        print("Thank you - password is valid")
        break
    else:
        print(password,"is not a valid password - try again")
        
        
        
        

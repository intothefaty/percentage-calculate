# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 14:33:24 2020

"""
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2

while(True):
    print("\n\nOperations:")
    print("1 : Addition")
    print("2 : Subtraction")
    print("3 : Multiplication")
    print("4 : Division")
    print("5 : Quit")
    
    secenek = input("Enter an operation : ")
    if secenek == '5':
        break
    
    num1 = int(input("First Number : "))
    num2 = int(input("Second Number : "))
    
    if secenek == '1':
        print("Addition : " +str(add(num1,num2)))
    elif secenek == '2':
        print("Subtraction : " +str(sub(num1,num2)))   
    elif secenek == '3':
        print("Multiplication : " +str(mul(num1,num2))) 
    elif secenek == '4':
        print("Division : " +str(div(num1,num2)))
    else:
        print("Invalid Option")











# -*- coding: utf-8 -*-

def fiboMoreThaN(x):
    y=0
    z=1
    if x==1:
        return z
    else:
        while z<=x:
            temp = z
            z+=y
            y=temp
        return z
    

a=1
while a>-1:
    a = int(input("\nEnter an integer number (<0 will stop inputting): "))
    if a>-1:
        print("First Fibonacci number > ",a,"is :",fiboMoreThaN(a))
    


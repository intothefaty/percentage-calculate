# -*- coding: utf-8 -*-

def fibonacciN(x):
    y=0
    z=1
    if x==1:
        return y
    elif x == 2:
        return z
    else:
        x-=1
        for i in range(x-1):
            temp = z
            z+=y
            y=temp
        return z
    

a=1
while a>0:
    a = int(input("Which Fibonacci number you want (<=0 will stop inputting)? "))
    if a>0:
        print("Fibonacci number",a,"is:",fibonacciN(a))
    


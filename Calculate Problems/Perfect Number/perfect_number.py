# -*- coding: utf-8 -*-

def is_perfect(x):
    x2 = 0
    for i in range(1,x):
        if (x%i)==0:
            x2=x2+i
    if (x==x2):
        return True
    else:
        return False
    

a = int(input("Input lowest search limit of perfect numbers: "))
b = int(input("Input highest search limit of perfect numbers: "))

counter = 0

if a>b:
    print("Range is not correct!")
else:
    print("The perfect numbers between",a,"and",b,"are : ", end="")
    for i in range(a+1,b):
        if is_perfect(i):
            counter+=1
            print(i,end=" ")
if counter == 0:
    print("None")
# -*- coding: utf-8 -*-

number = int(input("Number : "))

factorial = 1

if number<0:
    print("The factorial of negative numbers cannot be calculated")
elif number==0:
    print("Result : 1")
else:
    for i in range(1,number+1):
        factorial = factorial * i
    print("Result : ",factorial)
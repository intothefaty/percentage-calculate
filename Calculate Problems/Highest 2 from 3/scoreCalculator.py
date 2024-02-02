# -*- coding: utf-8 -*-

x = int(input("Enter first score: "))
y = int(input("Enter second score: "))
z = int(input("Enter third score: "))

if z<x and z<y:
    average = (x+y)/2
elif y<x and y<z:
    average = (x+z)/2
else:
    average = (y+z)/2

print("Average of two highest scores is",average)


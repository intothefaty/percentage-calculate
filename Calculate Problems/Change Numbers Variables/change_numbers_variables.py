# -*- coding: utf-8 -*-

x = int(input("Enter x : "))
y = int(input("Enter y : "))

x,y = y,x

# inefficient way
#temp = x
#x = y
#y = temp

print("x = " + str(x))
print("y = " + str(y))

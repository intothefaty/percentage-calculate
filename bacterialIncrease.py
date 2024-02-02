# -*- coding: utf-8 -*-

initial = int(input("Enter the initial number of bacterial cells: "))
final = int(input("Enter the final number of bacterial cells: "))

increasePer = ((final - initial)/initial)*100

print("Increase Percentage = %",int(increasePer))

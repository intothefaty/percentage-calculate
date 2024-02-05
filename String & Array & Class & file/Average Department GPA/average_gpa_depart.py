# -*- coding: utf-8 -*-

def read_file(fileName):
    f = open(fileName)
    
    stuD = {}
    
    for line in f.readlines():
        words = line.split()
        department = words[-2]
        CPGA = float(words[-1])
        if department in stuD:
            stuD[department]+=(CPGA,)
        else:
            stuD[department]=(CPGA,)
    
    return stuD

stuD = read_file("student.txt")

department = input("Enter Department Name: ")

try:
    average = sum(stuD[department])/len(stuD[department])
    print("Average CPGA of",department,"is",average)
except:
    print("No data for Department",department)


# -*- coding: utf-8 -*-

def read_file(fileName):
    f = open(fileName)
    
    stuD = {}
    
    for line in f.readlines():
        words = line.split(",")
        department = words[1]
        GGPA = words[2]
        student = words[0]
        if department in stuD:
            stuD[department]+=(student+","+GGPA,)
        else:
            stuD[department]=(student+","+GGPA,)
    
    return stuD

stuD = read_file("student_17998c2dd692b6d22243e6f54c5a7d61.txt")

name = input("Enter Student Name: ")

try:
    for dep, nc in stuD.items():
        for item in nc:
            if len(item)>len(name) and item[:len(name)].lower()==name.lower():
                department = dep
                GGPA = item.split(",")[1]
                
            
    print("Department is",department,"GGPA is",GGPA)
except:
    print("No such a student")

# -*- coding: utf-8 -*-

from ptWorker import PTWorker
from ftWorker import FTWorker

def read_file(fname):
    f=open(fname,"r")
    dict1={}
    
    for line in f:
        listt=line.strip().split()
        Id=listt[0]
        if listt[-1]=="PT":
            w = PTWorker(listt[1], listt[2], listt[3])
        else:
            w = FTWorker(listt[1], listt[2], listt[3])
        
        w.setSalary(w.calculateSalary())
        dict1[Id]=w
    return dict1

x=read_file("Worker.txt")

for key in x:
    print(key,x[key],"TL")
    x[key].increase(0.18)

y = input("Enter salary threshold: ")
print("Names of Workers Below the given threshold")
for key in x:
    if x[key].getSalary()<float(y):
        print(x[key].getName())
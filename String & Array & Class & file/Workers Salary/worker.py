# -*- coding: utf-8 -*-

class Worker():
    def __init__(self,name,salary=0):
        self.__name=name
        self.__salary=float(salary)
        
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def setSalary(self,salary):
        self.__salary=float(salary)
    def increase(self,rate):
        self.__salary=self.__salary*(1+rate)
    def __repr__(self):
        output = "Name: "+self.__name+"\t"+"Salary: "+str(self.__salary)
        return output
        
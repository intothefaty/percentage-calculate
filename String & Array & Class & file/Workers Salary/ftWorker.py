# -*- coding: utf-8 -*-

from worker import Worker

class FTWorker(Worker):
    def __init__(self,name,gross,foreign):
        super().__init__(name)
        self.__gross=int(gross)
        self.__foreign=foreign
        if foreign == "Y":
            self.__foreign==True
        else:
            self.__foreign==False
    
    def calculateSalary(self):
        tax = int(self.__gross)*0.15
        if self.__foreign==True:
            ext = self.__gross*0.08
        else:
            ext=0
        return self.__gross+ext-tax
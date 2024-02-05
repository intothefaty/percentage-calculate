# -*- coding: utf-8 -*-

from worker import Worker

class PTWorker(Worker):
    def __init__(self,name,hours,hourly):
        super().__init__(name)
        self.__hours=int(hours)
        self.__hourly=int(hourly)
    def calculateSalary(self):
        if self.__hours>40:
            return (40*self.__hourly)+((self.__hours-40)*self.__hourly*1.5)
        else:
            return int(self.__hours)*int(self.__hourly)

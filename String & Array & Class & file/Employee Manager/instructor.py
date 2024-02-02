# -*- coding: utf-8 -*-

class Instructor:
    __id = str
    __name = str
    __status = str
    __hours = int
    
    def __init__(self,_id,_name,_status,_hours):
        self.__id = _id
        self.__name = _name
        self.__status = _status
        self.__hours = _hours

    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_status(self):
        return self.__status
    def get_hours(self):
        return self.__hours
    def calculate_salary(self):
        if(self.__status=="F"):
            return 5000 + self.__hours*500
        else:
            return self.__hours*400



        
        

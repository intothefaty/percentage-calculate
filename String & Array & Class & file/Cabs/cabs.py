# -*- coding: utf-8 -*-

"""
 I created the "cab" class. It contains the type and kms variables.
 I entered assignments as constructor. 
 It compares the kms value of the object with the kms entered in the "__lt__" function, and returns -1, 0 and 1 values. 
 In the "__eq__" function I made the "if" return true and false if the kms and type values are the same. 
 I have printed the type and kms in the "__repr__" function. 
 I wrote a get function that returns self values in getType and getKms functions. 
 I defined the variable price_per_km in the "sedan" and "hatchback" classes, 
 and multiplied the lms and price_per_km variables in the calculate function and returned it.
"""

class Cab():
    __type = str
    __kms = int
    def __init__(self,typeofcab,kms):
        self.type = typeofcab
        self.kms = int(kms)
    
    def __lt__(self,kms):
        if (kms<self.kms):
            return -1
        elif (kms>self.kms):
            return 1
        else:
            return 0


    def __eq__(self,kms,typeofcab):
        if(kms==self.kms and self.type==typeofcab):
            return True
        else:
            return False
        
    def __repr__(self):
        print(self.type,self.kms)
        
    def getType(self):
        return self.type
    def getKms(self):
        return self.kms
    


class Sedan(Cab):
    __price_per_km = 2
    
    def __init__(self,typeofcab,kms):
        super.__init__(self, typeofcab, kms)
        
    def calculate_fare(self):
        return self.kms * self.price_per_km
        
class Hatchback(Cab):
    __price_per_km = 1.5
    
    def __init__(self,typeofcab,kms):
        super.__init__(self, typeofcab, kms)
        
    def calculate_fare(self):
        return self.kms * self.price_per_km
        




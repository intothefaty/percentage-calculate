# -*- coding: utf-8 -*-

def sumAllNumbers(numberList):
    result = 0
    
    for i in range(len(numberList)):
        result += numberList[i]
    
    return result
    
    
    




numberList = [5,7,10,35,27,65,3,0,1]
toplam = sumAllNumbers(numberList)
print(toplam)

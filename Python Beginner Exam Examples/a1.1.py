# -*- coding: utf-8 -*-

def isFibonacci(num):
    prev=0
    now=1
    nextNum=1
    if(num==0 or num==1):
        return True
    else:
        while(True):
            if(num<now):
                return False
            else:
                prev=now
                now=nextNum
                nextNum=prev+now
                if(num==now):
                    return True


x = int(input("Enter a number : "))

if(isFibonacci(x)):
    print(x, "is in the fibonacci sequence.")
else:
    print(x, "is not in the fibonacci sequence..")

                
        
    
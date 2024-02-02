# -*- coding: utf-8 -*-

'''
Calculate Cal
Cycling 200 cal
Running 475 cal
Swimming 275 cal

and

Classify with change metrics
'''

cycling = int(input("Enter number of hours cycling: "))
running = int(input("Enter number of hours running: "))
swimming = int(input("Enter number of hours swimming: "))

total = 200*cycling + 475*running + 275*swimming
print(total,"calories are burned")
if total<1750:
    print("No Significat Change")
elif total>3500:
    print("Significat Change")
else:
    print("Good Progress")
    

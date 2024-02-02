# -*- coding: utf-8 -*-

x = int(input("Enter your age: "))
y = int(input("Enter your resting heart rate: "))
z = int(input("Enter training heart rate: "))

targetHeartRate = 0.7*(220-x)+0.3*y

print("Target heart rate is",targetHeartRate,"beats/min")

if targetHeartRate<z:
    print("Lower your speed!")
else:
    print("Speed up!")
    
    
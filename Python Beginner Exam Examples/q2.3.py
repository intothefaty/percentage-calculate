# -*- coding: utf-8 -*-

# What is the output of this code

list1 = [0,1,2,3,4,5,6,7,8,9]

list2 = [0,0,0,0,0,0,0,0,0,0]

x=0

for i in range(1, len(list1), 2):
    list2[x] = list1[i]
    x+=1

for i in range(0, len(list1), 2):
    list2[x] = list1[i]
    x+=1

print(list2)
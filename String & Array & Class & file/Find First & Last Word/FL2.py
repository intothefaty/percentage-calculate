# -*- coding: utf-8 -*-

def form(str1):
    x=str1.find(" ")
    if x==-1:
        str2=str1+" "+str1
    else:
        y=str1.rfind(" ")
        str2=str1[:x] + str1[y:]
    return str2

a = input("Enter a sentence: ")

print("New String Formed from First and last words:",form(a.strip()))

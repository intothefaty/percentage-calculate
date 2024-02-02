# -*- coding: utf-8 -*-

def form(str1):
    temp=str1.split()
    str2 = temp[0] +" "+ temp[len(temp)-1]
    return str2

a = input("Enter a sentence: ")

print("New String Formed from First and last words:",form(a))


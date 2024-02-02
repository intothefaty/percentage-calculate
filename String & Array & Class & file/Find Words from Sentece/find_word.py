# -*- coding: utf-8 -*-

def wordsStart(s1,ch):
    s2=""
    cond=False
    for i in range(0,len(s1),1):
        if s1[i]==ch:
            cond=True
        if cond==1:
            s2+=s1[i]
        if s1[i]==" ":
            cond = False
        
    return s2



s1 = input("Sentence: ")
ch = input("Character: ")
print("Result :", wordsStart(s1, ch))

# -*- coding: utf-8 -*-

def separate(productList):
    vegetables = []
    flowers = []
    for i in range(len(productList)):
        x=len(productList[i])
        if productList[i][x-2]=="V":
            vegetables.append(productList[i][:x-3])
        else:
            flowers.append(productList[i][:x-3])
            
    print("Flowers: ",flowers)
    print("Vegetables: ",vegetables)
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:55:28 2022

@author: user
"""
from product_class import Product

def create_products(filename):
    l = []
    file = open(filename, 'r')
    for line in file:
        a = line.split()
        l.append(Product(float(a[0]), a[1]))
    file.close()
    return l
        
        
def find_product(l):
    a = l[:]
    if len(a)<2:
        return a
    elif a[0] < a[1]:
        a.pop(0)
    else:
        a.pop(1)
    return find_product(a)

def selectionSortDescending(l):
    a = 0
    while a != len(l):
        for i in range(a, len(l)):
            if l[a].get_price() < l[i].get_price():
                l[a], l[i] = l[i], l[a]
        a += 1
        
        
        
a = create_products('products.txt')
print('Products:\n', a)

y = find_product(a)
print('Maximum Product:\n', y)

selectionSortDescending(a)
print('Products sorted by price:\n', a)
a.sort()
print('Products sorted by date:\n', a)

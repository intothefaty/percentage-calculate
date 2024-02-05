# -*- coding: utf-8 -*-

import datetime

class Product:
    __productCounter = 10000
    def __init__(self, price, date = datetime.datetime.now()):
        
        self.__productId = f'{datetime.datetime.now().year}-{Product.__productCounter}'
        Product.__productCounter += 1
        self.__productPrice = price
        self.setExpiryDate( date )
    
    def get_price(self):
        return self.__productPrice
    
    def setProductId(self,product_id):
        self.__productId = product_id
    
    
    def formatExpiryDate(self):        
        return f'{self.__product_date.year}-{self.__product_date.month}-{self.__product_date.day}'
    
    
    
    def __str__(self):
        return f'{self.__productId}: {self.__productPrice}TL ({self.formatExpiryDate()})'
    
    def __repr__(self):
        return f'{self.__productId}: {self.__productPrice}TL ({self.formatExpiryDate()})\n'


    def setExpiryDate(self, product_date):
        if isinstance(product_date, datetime.datetime):
            self.__product_date = product_date
            
        else:
            a = product_date.split('/')
            self.__product_date = datetime.datetime(int(a[0]), int(a[1]), int(a[2]))
     
        
    def __add__(self, other):
        if isinstance(other, Product):
            Sum = self.__productPrice + other.get_price()
            a = Product(Sum)
            return a
        else:
            b = Product(self.__productPrice, self.__product_date)
            b.setProductId(self.__ProductId)
            return b
    def __lt__(self, other):
        if self.__productPrice < other.__productPrice:
            return True
        else:
            return False
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
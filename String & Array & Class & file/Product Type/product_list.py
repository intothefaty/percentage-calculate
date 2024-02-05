# -*- coding: utf-8 -*-

import module

f = open("product.txt")
productList = f.readlines()
f.close()



module.separate(productList)
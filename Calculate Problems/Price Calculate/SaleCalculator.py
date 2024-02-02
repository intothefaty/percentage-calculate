# -*- coding: utf-8 -*-

firstSuit = int(input("Enter cost of first suit: "))
secondSuit = int(input("Enter cost of second suit: "))

if firstSuit<secondSuit:
    lowPriceSuit=firstSuit
    highPriceSuit=secondSuit
else:
    lowPriceSuit=secondSuit
    highPriceSuit=firstSuit

total = highPriceSuit+lowPriceSuit/2

print("Cost of the two suits is",total,"TL")

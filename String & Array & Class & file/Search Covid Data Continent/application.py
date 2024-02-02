# -*- coding: utf-8 -*-

import os
import module as script

input_file="covid_country.txt"
data_file="covid_data.txt"
output_file="output.txt"

continent = input("Enter continent: ")
script.extract_data(input_file, data_file, output_file, continent)
continent_file = continent+".txt"

f = open(continent_file,"a")
f2= open(output_file)

for line in f2.readlines():
    f.write(line)

f.close()
f2.close()
total = script.calculate_total(continent_file)
print("Case, Death, Tests: " + total)

a=input("Remove created files [y][n]: ")
if a=="y":
    os.remove(continent_file)
    os.remove("output.txt")

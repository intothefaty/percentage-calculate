# -*- coding: utf-8 -*-
import os
import script

def extract_data(inpFileName,dataFileName,outpFileName):
    f = open(inpFileName)
    dRateFileName = script.createDeathRateFile(dataFileName)
    f2 = open(dRateFileName)
    f3 = open(outpFileName,"a")

    for line in f.readlines():
        
        x=line.find("\t")
        f3.write(line[:x]+"\t"+f2.readline())

    f3.close()
    f2.close()
    f.close()
    return outpFileName

def find_income(country,fname):
    message =""
    f=open(fname)
    for line in f.readlines():
        x=line.find("\t")
        
        if country.upper()==line[:x].upper():
            dRate = round(float(line[x+1:]),2)
            message="Death Percentage for "+country+" is "+str(dRate)+"%"
    return message
    
    
    

fname = extract_data("covid_country.txt", "covid_data.txt", "output.txt")

country=""

while country!="quit":
    country = input("Enter country to search (quit to exit): ")
    if country.lower() !="quit":
        message = find_income(country, fname)
        if message =="":
            print("No data for "+country+"...")
        else:
            print(message)
    
dFunc=input("Delete created files [y] or [n] : ")
if dFunc=="y":
    os.remove("death_rates.txt")
    os.remove("output.txt")

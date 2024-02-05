# -*- coding: utf-8 -*-



def createDeathRateFile(dataFileName):
    f = open(dataFileName)
    f2 = open("death_rates.txt","a")

    for line in f.readlines():
        x=line.find(" ")
        y=line.rfind(" ")
        infected=int(line[0:x])
        death=int(line[x+1:y])
        dRate=death/infected
        f2.write(str(dRate*100)+"\n")

    f2.close()
    f.close()
    return "death_rates.txt"
